# =============================================================================
# conftest.py
# Shared pytest fixtures — driver lifecycle, login, page objects
# =============================================================================

import pytest
import logging
import os

from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.patients_page import PatientsPage
from pages.new_prescription_page import NewPrescriptionPage
from pages.patient_history_page import PatientHistoryPage
from pages.medicines_page import MedicinesPage
from pages.medicine_details_page import MedicineDetailsPage
from pages.reports_page import ReportsPage
from pages.users_page import UsersPage

logger = logging.getLogger(__name__)

# ── Ensure output directories exist ───────────────────────────────────────────
os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
os.makedirs(Config.REPORT_DIR,     exist_ok=True)


# ==============================================================================
# DRIVER FIXTURE  (function scope — fresh browser per test)
# ==============================================================================

@pytest.fixture(scope="function")
def driver():
    """Provide a fresh WebDriver instance for each test. Quit after test ends."""
    drv = DriverFactory.get_driver()
    logger.info("Browser started")
    yield drv
    drv.quit()
    logger.info("Browser closed")


# ==============================================================================
# AUTHENTICATED DRIVER FIXTURE
# ==============================================================================

@pytest.fixture(scope="function")
def auth_driver(driver):
    """
    Provide a driver that is already logged in as admin.
    Use this fixture instead of `driver` for any test that requires login.
    """
    login = LoginPage(driver)
    login.open()
    login.login_as_admin()

    # Wait until dashboard is reached
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
        EC.url_contains("dashboard.php")
    )
    logger.info("Logged in as admin — dashboard reached")
    return driver


# ==============================================================================
# PAGE OBJECT FIXTURES  (all use auth_driver)
# ==============================================================================

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def dashboard_page(auth_driver):
    return DashboardPage(auth_driver)


@pytest.fixture
def patients_page(auth_driver):
    page = PatientsPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def new_prescription_page(auth_driver):
    page = NewPrescriptionPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def patient_history_page(auth_driver):
    page = PatientHistoryPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def medicines_page(auth_driver):
    page = MedicinesPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def medicine_details_page(auth_driver):
    page = MedicineDetailsPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def reports_page(auth_driver):
    page = ReportsPage(auth_driver)
    page.open()
    return page


@pytest.fixture
def users_page(auth_driver):
    page = UsersPage(auth_driver)
    page.open()
    return page


# ==============================================================================
# AUTO-SCREENSHOT ON FAILURE
# ==============================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("auth_driver")
        if driver:
            test_name = item.name.replace(" ", "_")
            path = os.path.join(Config.SCREENSHOT_DIR, f"FAIL_{test_name}.png")
            driver.save_screenshot(path)
            logger.warning(f"Failure screenshot: {path}")
