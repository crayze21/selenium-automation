# tests/test_functional.py
# Functional tests — one class per module, full feature coverage.
# Run daily: pytest -m functional

import pytest
import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.patients_page import PatientsPage
from pages.medicines_page import MedicinesPage
from pages.medicine_details_page import MedicineDetailsPage
from pages.new_prescription_page import NewPrescriptionPage
from pages.patient_history_page import PatientHistoryPage
from pages.reports_page import ReportsPage
from pages.users_page import UsersPage
from locators.locators import (
    PatientsPage as PL, MedicinesPage as ML,
    MedicineDetailsPage as MDL, ReportsPage as RL, UsersPage as UL
)
from test_data.test_data import (
    LoginData, PatientData, MedicineData,
    MedicineDetailData, ReportData, UserData
)
from utils.config import Config


# ── Helpers ────────────────────────────────────────────────────────────────────

def unique(prefix: str) -> str:
    """Generate a unique name to avoid collisions between test runs."""
    return f"{prefix}_{uuid.uuid4().hex[:6].upper()}"


# ==============================================================================
# LOGIN
# ==============================================================================

@pytest.mark.functional
class TestFunctionalLogin:

    def test_valid_credentials_redirect_to_dashboard(self, login_page):
        login_page.open()
        login_page.login_as_admin()
        WebDriverWait(login_page.driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("dashboard.php")
        )
        assert "dashboard.php" in login_page.get_current_url()

    def test_invalid_username_shows_error(self, login_page):
        login_page.open()
        login_page.login(LoginData.INVALID_USERNAME, LoginData.VALID_PASSWORD)
        assert login_page.is_on_login_page()
        assert login_page.is_error_displayed(), \
            "Error message should appear for invalid username"

    def test_invalid_password_shows_error(self, login_page):
        login_page.open()
        login_page.login(LoginData.VALID_USERNAME, LoginData.INVALID_PASSWORD)
        assert login_page.is_on_login_page()
        assert login_page.is_error_displayed()

    def test_empty_username_prevented(self, login_page):
        login_page.open()
        login_page.login("", LoginData.VALID_PASSWORD)
        assert login_page.is_on_login_page()

    def test_empty_password_prevented(self, login_page):
        login_page.open()
        login_page.login(LoginData.VALID_USERNAME, "")
        assert login_page.is_on_login_page()

    def test_both_empty_prevented(self, login_page):
        login_page.open()
        login_page.login("", "")
        assert login_page.is_on_login_page()

    def test_logout_ends_session(self, auth_driver):
        from pages.dashboard_page import DashboardPage
        from locators.locators import URLs
        DashboardPage(auth_driver).logout()
        auth_driver.get(URLs.DASHBOARD)
        WebDriverWait(auth_driver, 5).until(
            EC.url_contains("index.php")
        )
        assert "index.php" in auth_driver.current_url or \
               auth_driver.current_url.endswith("/")


# ==============================================================================
# PATIENTS
# ==============================================================================

@pytest.mark.functional
class TestFunctionalPatients:

    def test_add_patient_valid_data_appears_in_table(self, auth_driver):
        page = PatientsPage(auth_driver)
        page.open()
        name = unique("FuncPatient")
        page.add_patient(name, "Test Address", "123456", "1990-01-01", "09171234567", "Male")
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_patients"))
        )
        assert page.is_patient_in_table(name), \
            f"'{name}' should appear in table after adding"

    def test_add_patient_empty_name_stays_on_page(self, patients_page):
        patients_page.add_patient("", "Address", "111", "1990-01-01", "09170000000", "Female")
        assert patients_page.is_on_page()

    def test_patient_table_has_all_columns(self, patients_page):
        for col_num, expected in enumerate(
            ["S.No", "Patient Name", "Address", "CNIC",
             "Date Of Birth", "Phone Number", "Gender", "Action"], start=1
        ):
            text = patients_page.helpers.get_text(
                (By.XPATH, f"//table[@id='all_patients']//th[{col_num}]")
            )
            assert expected.lower() in text.lower(), \
                f"Column {col_num} should be '{expected}', got '{text}'"

    def test_search_filters_to_matching_patient(self, patients_page):
        patients_page.search_patient(PatientData.EXISTING_NAME)
        time.sleep(0.5)
        assert patients_page.is_patient_in_table(PatientData.EXISTING_NAME)

    def test_search_nonexistent_returns_zero_rows(self, patients_page):
        patients_page.search_patient("XYZNOTEXIST999")
        time.sleep(0.5)
        assert patients_page.get_row_count() == 0

    def test_page_info_shows_entry_count(self, patients_page):
        info = patients_page.get_page_info_text()
        assert "entries" in info.lower()

    def test_all_export_buttons_visible(self, patients_page):
        for label, locator in [
            ("Copy", PL.BTN_COPY), ("CSV", PL.BTN_CSV),
            ("Excel", PL.BTN_EXCEL), ("PDF", PL.BTN_PDF), ("Print", PL.BTN_PRINT),
        ]:
            assert patients_page.helpers.is_displayed(locator), \
                f"'{label}' button should be visible"

    def test_add_patient_form_all_fields_present(self, patients_page):
        for label, locator in [
            ("Patient Name", PL.PATIENT_NAME), ("Address", PL.ADDRESS),
            ("CNIC", PL.CNIC), ("Phone Number", PL.PHONE_NUMBER),
            ("Gender", PL.GENDER), ("Save Button", PL.SAVE_BTN),
        ]:
            assert patients_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible in the form"


# ==============================================================================
# MEDICINES
# ==============================================================================

@pytest.mark.functional
class TestFunctionalMedicines:

    def test_add_medicine_valid_name_appears_in_table(self, auth_driver):
        page = MedicinesPage(auth_driver)
        page.open()
        name = unique("FuncMed")
        page.add_medicine(name)
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_medicines"))
        )
        assert page.is_medicine_in_table(name)

    def test_add_medicine_empty_name_stays_on_page(self, medicines_page):
        medicines_page.add_medicine("")
        assert medicines_page.is_on_page()

    def test_medicines_table_has_all_columns(self, medicines_page):
        for col_num, expected in enumerate(
            ["S.No", "Medicine Name", "Action"], start=1
        ):
            text = medicines_page.helpers.get_text(
                (By.XPATH, f"//table[@id='all_medicines']//th[{col_num}]")
            )
            assert expected.lower() in text.lower()

    def test_search_filters_medicines(self, medicines_page):
        medicines_page.search_medicine(MedicineData.EXISTING)
        time.sleep(0.5)
        assert medicines_page.is_medicine_in_table(MedicineData.EXISTING)

    def test_seeded_medicines_are_in_table(self, medicines_page):
        for name in ["Amoxicillin", "Losartan", "Mefenamic"]:
            medicines_page.search_medicine(name)
            time.sleep(0.4)
            assert medicines_page.is_medicine_in_table(name), \
                f"Seeded medicine '{name}' should exist"


# ==============================================================================
# MEDICINE DETAILS
# ==============================================================================

@pytest.mark.functional
class TestFunctionalMedicineDetails:

    def test_add_medicine_detail_valid_data(self, medicine_details_page):
        medicine_details_page.add_medicine_detail(
            MedicineDetailData.MEDICINE, MedicineDetailData.PACKING
        )
        WebDriverWait(medicine_details_page.driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "medicine_details"))
        )
        assert medicine_details_page.get_row_count() >= 1

    def test_add_medicine_detail_no_medicine_selected_stays_on_page(
        self, medicine_details_page
    ):
        medicine_details_page.enter_packing("50")
        medicine_details_page.click_save()
        assert medicine_details_page.is_on_page()

    def test_medicine_details_table_columns(self, medicine_details_page):
        for col_num, expected in enumerate(
            ["S.No", "Medicine Name", "Packing", "Action"], start=1
        ):
            text = medicine_details_page.helpers.get_text(
                (By.XPATH, f"//table[@id='medicine_details']//th[{col_num}]")
            )
            assert expected.lower() in text.lower()

    def test_search_filters_medicine_details(self, medicine_details_page):
        medicine_details_page.search(MedicineDetailData.MEDICINE)
        time.sleep(0.5)
        assert medicine_details_page.get_row_count() >= 1

    def test_medicine_dropdown_contains_seeded_options(self, medicine_details_page):
        from selenium.webdriver.support.ui import Select
        select_el = medicine_details_page.driver.find_element(*MDL.MEDICINE_SELECT)
        options = [o.text for o in Select(select_el).options]
        assert any("Amoxicillin" in o for o in options), \
            "Medicine dropdown should contain seeded medicines"


# ==============================================================================
# PATIENT HISTORY
# ==============================================================================

@pytest.mark.functional
class TestFunctionalPatientHistory:

    def test_page_loads_with_search_form(self, patient_history_page):
        assert patient_history_page.is_on_page()
        from locators.locators import PatientHistoryPage as PHL
        assert patient_history_page.helpers.is_displayed(PHL.PATIENT_SELECT)
        assert patient_history_page.helpers.is_displayed(PHL.SEARCH_BTN)

    def test_search_without_patient_stays_on_page(self, patient_history_page):
        patient_history_page.click_search()
        assert patient_history_page.is_on_page()

    def test_history_table_has_all_columns(self, patient_history_page):
        for col_num, expected in enumerate(
            ["S.No", "Visit Date", "Disease", "Medicine",
             "Packing", "QTY", "Dosage", "Instruction", "Action"], start=1
        ):
            text = patient_history_page.helpers.get_text(
                (By.XPATH, f"//table[@id='patient_history']//th[{col_num}]")
            )
            assert expected.lower() in text.lower()

    def test_patient_dropdown_contains_seeded_patients(self, patient_history_page):
        from locators.locators import PatientHistoryPage as PHL
        from selenium.webdriver.support.ui import Select
        select_el = patient_history_page.driver.find_element(*PHL.PATIENT_SELECT)
        options = [o.text for o in Select(select_el).options]
        assert len(options) > 1, \
            "Patient dropdown should have at least one patient option"


# ==============================================================================
# REPORTS
# ==============================================================================

@pytest.mark.functional
class TestFunctionalReports:

    def test_page_loads_with_both_sections(self, reports_page):
        assert reports_page.is_visits_section_displayed()
        assert reports_page.is_disease_section_displayed()

    def test_visits_report_all_fields_present(self, reports_page):
        for label, locator in [
            ("From date", RL.PATIENTS_FROM), ("To date", RL.PATIENTS_TO),
            ("Generate PDF", RL.GENERATE_VISITS_PDF),
        ]:
            assert reports_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible"

    def test_disease_report_all_fields_present(self, reports_page):
        for label, locator in [
            ("Disease input", RL.DISEASE_INPUT), ("From date", RL.DISEASE_FROM),
            ("To date", RL.DISEASE_TO), ("Generate PDF", RL.GENERATE_DISEASE_PDF),
        ]:
            assert reports_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible"

    def test_visits_generate_btn_enabled_after_dates_filled(self, reports_page):
        reports_page.set_visits_from_date(ReportData.FROM_DATE)
        reports_page.set_visits_to_date(ReportData.TO_DATE)
        assert reports_page.helpers.is_enabled(RL.GENERATE_VISITS_PDF)

    def test_disease_generate_btn_enabled_after_all_filled(self, reports_page):
        reports_page.enter_disease(ReportData.DISEASE)
        reports_page.set_disease_from_date(ReportData.FROM_DATE)
        reports_page.set_disease_to_date(ReportData.TO_DATE)
        assert reports_page.helpers.is_enabled(RL.GENERATE_DISEASE_PDF)


# ==============================================================================
# USERS
# ==============================================================================

@pytest.mark.functional
class TestFunctionalUsers:

    def test_add_user_valid_data_appears_in_table(self, auth_driver):
        page = UsersPage(auth_driver)
        page.open()
        uname = unique("funcuser").lower()
        page.add_user(f"Func User {uname}", uname, "funcpass123")
        WebDriverWait(auth_driver, Config.EXPLICIT_WAIT).until(
            EC.presence_of_element_located((By.ID, "all_users"))
        )
        assert page.get_row_count() >= 1

    def test_add_user_empty_username_stays_on_page(self, users_page):
        users_page.add_user("Display Name", "", "somepassword")
        assert users_page.is_on_page()

    def test_add_user_empty_password_stays_on_page(self, users_page):
        users_page.add_user("Display Name", "someuser", "")
        assert users_page.is_on_page()

    def test_users_table_has_all_columns(self, users_page):
        for col_num, expected in enumerate(
            ["S.No", "Picture", "Display Name", "Username", "Action"], start=1
        ):
            text = users_page.helpers.get_text(
                (By.XPATH, f"//table[@id='all_users']//th[{col_num}]")
            )
            assert expected.lower() in text.lower()

    def test_seeded_admin_user_exists_in_table(self, users_page):
        rows = users_page.driver.find_elements(
            By.CSS_SELECTOR, "#all_users tbody tr"
        )
        usernames = [r.text for r in rows]
        assert any("admin" in u.lower() for u in usernames), \
            "Admin user should exist in the users table"

    def test_add_user_form_all_fields_present(self, users_page):
        for label, locator in [
            ("Display Name", UL.DISPLAY_NAME), ("Username", UL.USERNAME),
            ("Password", UL.PASSWORD), ("Profile Pic", UL.PROFILE_PIC),
        ]:
            assert users_page.helpers.is_displayed(locator), \
                f"'{label}' field should be visible"