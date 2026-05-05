# tests/test_smoke.py
# Smoke tests — fast sanity checks, one per module.
# Run these on every deploy: pytest -m smoke

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.patients_page import PatientsPage
from pages.medicines_page import MedicinesPage
from pages.medicine_details_page import MedicineDetailsPage
from pages.new_prescription_page import NewPrescriptionPage
from pages.patient_history_page import PatientHistoryPage
from pages.reports_page import ReportsPage
from pages.users_page import UsersPage
from locators.locators import NavBar
from utils.config import Config


@pytest.mark.smoke
class TestSmoke:
    """
    One test per module. Each test:
      - navigates to the page
      - asserts the page loaded (correct URL or heading)
      - asserts the single most important element is visible
    No form submissions. No data creation. Pure visibility checks.
    """

    def test_smoke_login_page_loads(self, login_page):
        login_page.open()
        assert login_page.is_on_login_page()
        assert login_page.helpers.is_displayed(
            (By.NAME, "login")
        ), "Login button must be visible"

    def test_smoke_valid_login(self, login_page):
        login_page.open()
        login_page.login_as_admin()
        WebDriverWait(login_page.driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("dashboard.php")
        )
        assert "dashboard.php" in login_page.get_current_url()

    def test_smoke_dashboard_loads(self, dashboard_page):
        assert dashboard_page.is_on_dashboard()
        assert dashboard_page.is_today_box_displayed()

    def test_smoke_patients_page_loads(self, auth_driver):
        page = PatientsPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "all_patients")
        ), "Patients table must be visible"

    def test_smoke_medicines_page_loads(self, auth_driver):
        page = MedicinesPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "all_medicines")
        ), "Medicines table must be visible"

    def test_smoke_medicine_details_page_loads(self, auth_driver):
        page = MedicineDetailsPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "medicine_details")
        ), "Medicine details table must be visible"

    def test_smoke_new_prescription_page_loads(self, auth_driver):
        page = NewPrescriptionPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "add_row")
        ), "Add row button must be visible"

    def test_smoke_patient_history_page_loads(self, auth_driver):
        page = PatientHistoryPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "search")
        ), "Search button must be visible"

    def test_smoke_reports_page_loads(self, auth_driver):
        page = ReportsPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "print_visits")
        ), "Generate visits PDF button must be visible"

    def test_smoke_users_page_loads(self, auth_driver):
        page = UsersPage(auth_driver)
        page.open()
        assert page.is_on_page()
        assert page.helpers.is_displayed(
            (By.ID, "all_users")
        ), "Users table must be visible"

    def test_smoke_sidebar_all_links_present(self, dashboard_page):
        for label, locator in [
            ("Dashboard",  NavBar.MENU_DASHBOARD_LINK),
            ("Patients",   NavBar.MENU_PATIENTS_LINK),
            ("Medicines",  NavBar.MENU_MEDICINES_LINK),
            ("Reports",    NavBar.MENU_REPORTS_LINK),
            ("Users",      NavBar.MENU_USERS_LINK),
            ("Logout",     NavBar.LOGOUT_LINK),
        ]:
            assert dashboard_page.helpers.is_displayed(locator), \
                f"Sidebar link '{label}' must be visible"

    def test_smoke_logout_works(self, auth_driver):
        page = DashboardPage(auth_driver)
        page.logout()
        assert "index.php" in auth_driver.current_url or \
               auth_driver.current_url.endswith("/"), \
               "Should be on login page after logout"