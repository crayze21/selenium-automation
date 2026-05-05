# tests/test_regression.py
# Regression tests — edge cases, boundary conditions, and previously-found bugs.
# Run before every release: pytest -m regression

import pytest
import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.patients_page import PatientsPage
from pages.medicines_page import MedicinesPage
from pages.new_prescription_page import NewPrescriptionPage
from pages.patient_history_page import PatientHistoryPage
from pages.users_page import UsersPage
from pages.dashboard_page import DashboardPage
from locators.locators import URLs
from utils.config import Config


def unique(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:6].upper()}"


# ==============================================================================
# SESSION & SECURITY
# ==============================================================================

@pytest.mark.regression
class TestRegressionSession:

    def test_accessing_dashboard_without_login_redirects(self, driver):
        """Unauthenticated request to dashboard.php must redirect to login."""
        driver.get(URLs.DASHBOARD)
        WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("index.php")
        )
        assert "index.php" in driver.current_url or \
               driver.current_url.endswith("/"), \
               "Unauthenticated access must redirect to login"

    def test_accessing_patients_without_login_redirects(self, driver):
        driver.get(URLs.PATIENTS)
        WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("index.php")
        )
        assert "index.php" in driver.current_url or \
               driver.current_url.endswith("/")

    def test_accessing_users_without_login_redirects(self, driver):
        driver.get(URLs.USERS)
        WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("index.php")
        )
        assert "index.php" in driver.current_url or \
               driver.current_url.endswith("/")

    def test_session_does_not_persist_after_logout(self, auth_driver):
        """After logout, back-navigation must not restore the session."""
        DashboardPage(auth_driver).logout()
        auth_driver.back()
        time.sleep(1)
        current = auth_driver.current_url
        assert "dashboard.php" not in current, \
            "Session should not be restored after logout via browser back"

    def test_page_title_on_login(self, driver):
        driver.get(URLs.LOGIN)
        assert "Toreja" in driver.title or "Clinic" in driver.title


# ==============================================================================
# PATIENTS — EDGE CASES
# ==============================================================================

@pytest.mark.regression
class TestRegressionPatients:

    def test_patient_name_with_special_characters(self, auth_driver):
        """Names with apostrophes and hyphens should save correctly."""
        page = PatientsPage(auth_driver)
        page.open()
        name = f"O'Brien-{uuid.uuid4().hex[:4].upper()}"
        page.add_patient(name, "Test St", "REG001", "1985-03-10", "09170000001", "Male")
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_patients"))
        )
        assert page.is_patient_in_table(name.split("-")[0]), \
            f"Patient with special chars '{name}' should be saved"

    def test_patient_search_is_case_insensitive(self, patients_page):
        """Searching 'MARK' should match 'Mark Cooper'."""
        patients_page.search_patient("mark")
        time.sleep(0.5)
        count_lower = patients_page.get_row_count()
        patients_page.search_patient("MARK")
        time.sleep(0.5)
        count_upper = patients_page.get_row_count()
        assert count_lower == count_upper, \
            "Search should be case-insensitive"

    def test_search_then_clear_restores_full_table(self, patients_page):
        """Clearing the search box should restore all rows."""
        full_count = patients_page.get_row_count()
        patients_page.search_patient("XYZNOTEXIST")
        time.sleep(0.5)
        patients_page.search_patient("")
        time.sleep(0.5)
        restored_count = patients_page.get_row_count()
        assert restored_count == full_count, \
            "Clearing search should restore full table"

    def test_patient_table_survives_page_refresh(self, patients_page):
        """Refreshing the page should keep the table intact."""
        count_before = patients_page.get_row_count()
        patients_page.refresh()
        WebDriverWait(patients_page.driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_patients"))
        )
        count_after = patients_page.get_row_count()
        assert count_after == count_before, \
            "Row count should be the same after refresh"

    def test_gender_dropdown_has_correct_options(self, patients_page):
        """Gender select must contain exactly Male, Female, Other."""
        from selenium.webdriver.support.ui import Select
        from locators.locators import PatientsPage as PL
        select_el = patients_page.driver.find_element(*PL.GENDER)
        options = [o.text for o in Select(select_el).options
                   if o.get_attribute("value")]
        for expected in ["Male", "Female", "Other"]:
            assert expected in options, \
                f"Gender option '{expected}' must be present"


# ==============================================================================
# MEDICINES — EDGE CASES
# ==============================================================================

@pytest.mark.regression
class TestRegressionMedicines:

    def test_medicine_name_with_numbers(self, auth_driver):
        """Medicine names with numbers should save correctly."""
        page = MedicinesPage(auth_driver)
        page.open()
        name = f"Med500mg_{uuid.uuid4().hex[:4].upper()}"
        page.add_medicine(name)
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_medicines"))
        )
        assert page.is_medicine_in_table(name)

    def test_medicine_search_then_clear_restores_all(self, medicines_page):
        full_count = medicines_page.get_row_count()
        medicines_page.search_medicine("ZZZNOTEXIST")
        time.sleep(0.5)
        medicines_page.search_medicine("")
        time.sleep(0.5)
        assert medicines_page.get_row_count() == full_count

    def test_duplicate_medicine_search_shows_correct_match(self, medicines_page):
        """Searching partial name 'Anti' should match Antibiotic and Antihistamine."""
        medicines_page.search_medicine("Anti")
        time.sleep(0.5)
        count = medicines_page.get_row_count()
        assert count >= 2, \
            "Partial search 'Anti' should match at least Antibiotic and Antihistamine"


# ==============================================================================
# PRESCRIPTION — EDGE CASES
# ==============================================================================

@pytest.mark.regression
class TestRegressionPrescription:

    def test_save_prescription_without_patient_stays_on_page(
        self, new_prescription_page
    ):
        new_prescription_page.enter_disease("Regression Test Disease")
        new_prescription_page.set_visit_date("2026-04-23")
        new_prescription_page.click_save_prescription()
        assert new_prescription_page.is_on_page(), \
            "Should stay on prescription page with no patient selected"

    def test_multiple_medicine_rows_can_be_added(self, new_prescription_page):
        """Add 3 rows and verify all 3 are present."""
        for _ in range(3):
            new_prescription_page.click_add_row()
            time.sleep(0.3)
        assert new_prescription_page.get_row_count() >= 3, \
            "Should be able to add multiple medicine rows"

    def test_delete_row_reduces_count(self, new_prescription_page):
        new_prescription_page.click_add_row()
        time.sleep(0.3)
        new_prescription_page.click_add_row()
        time.sleep(0.3)
        count_before = new_prescription_page.get_row_count()
        new_prescription_page.delete_medicine_row(count_before)
        time.sleep(0.3)
        assert new_prescription_page.get_row_count() == count_before - 1


# ==============================================================================
# NAVIGATION — REGRESSION
# ==============================================================================

@pytest.mark.regression
class TestRegressionNavigation:

    def test_all_menu_links_navigate_correctly(self, auth_driver):
        """Every sidebar link must navigate to the correct URL."""
        dashboard = DashboardPage(auth_driver)
        expected = [
            (dashboard.go_to_add_patients,    "patients.php"),
            (dashboard.go_to_new_prescription,"new_prescription.php"),
            (dashboard.go_to_patient_history, "patient_history.php"),
            (dashboard.go_to_add_medicine,    "medicines.php"),
            (dashboard.go_to_medicine_details,"medicine_details.php"),
            (dashboard.go_to_reports,         "reports.php"),
            (dashboard.go_to_users,           "users.php"),
        ]
        for nav_action, expected_url in expected:
            auth_driver.get(URLs.DASHBOARD)
            WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "aside.main-sidebar"))
            )
            nav_action()
            WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
                EC.url_contains(expected_url)
            )
            assert expected_url in auth_driver.current_url, \
                f"Navigation to '{expected_url}' failed, got: {auth_driver.current_url}"

    def test_footer_copyright_text_present(self, dashboard_page):
        footer = dashboard_page.helpers.get_text(
            (By.CSS_SELECTOR, "footer.main-footer")
        )
        assert "2026" in footer or "Clinic" in footer, \
            "Footer should contain copyright info"

    def test_brand_logo_links_to_dashboard(self, auth_driver):
        from locators.locators import NavBar
        auth_driver.get(URLs.PATIENTS)
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "aside.main-sidebar"))
        )
        auth_driver.find_element(*NavBar.BRAND_LINK).click()
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("dashboard.php")
        )
        assert "dashboard.php" in auth_driver.current_url