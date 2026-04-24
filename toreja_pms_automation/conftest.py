# =============================================================================
# conftest.py
# Shared pytest fixtures — driver lifecycle, login, page objects
# =============================================================================

import pytest
import logging
import os
from datetime import datetime

from utils.driver_factory import DriverFactory
from utils.config import Config
from utils.logger import get_logger
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
    logger.info("=" * 60)
    logger.info("Browser session starting")
    drv = DriverFactory.get_driver()
    yield drv
    logger.info("Browser session closing")
    logger.info("=" * 60)
    drv.quit()


# ==============================================================================
# AUTHENTICATED DRIVER FIXTURE
# ==============================================================================

@pytest.fixture(scope="function")
def auth_driver(driver):
    """
    Provide a driver that is already logged in as admin.
    Use this fixture instead of `driver` for any test that requires login.
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    logger.info("Logging in as admin")
    login = LoginPage(driver)
    login.open()
    login.login_as_admin()
    WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
        EC.url_contains("dashboard.php")
    )
    logger.info("Login successful — dashboard reached")
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
# ── Failure capture hook ───────────────────────────────────────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    # Find the driver from any fixture name that could hold it
    driver = None
    for name in ("driver", "auth_driver"):
        driver = item.funcargs.get(name)
        if driver:
            break

    if not driver:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = item.nodeid.replace("/", "_").replace("::", "_").replace(" ", "_")

    # 1. Screenshot
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    screenshot_path = os.path.join(
        Config.SCREENSHOT_DIR, f"FAIL_{safe_name}_{timestamp}.png"
    )
    try:
        driver.save_screenshot(screenshot_path)
        logger.warning(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        logger.error(f"Could not save screenshot: {e}")
        screenshot_path = None

    # 2. Page source
    source_path = os.path.join(
        Config.SCREENSHOT_DIR, f"FAIL_{safe_name}_{timestamp}.html"
    )
    try:
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        logger.warning(f"Page source saved: {source_path}")
    except Exception as e:
        logger.error(f"Could not save page source: {e}")
        source_path = None

    # 3. Log current URL
    try:
        current_url = driver.current_url
        logger.error(f"Failure URL: {current_url}")
    except Exception:
        current_url = "unknown"

    # 4. Attach everything to pytest-html report
    try:
        import pytest_html
        extras = getattr(report, "extras", [])
        if screenshot_path:
            extras.append(pytest_html.extras.image(screenshot_path))
        if source_path:
            extras.append(pytest_html.extras.url(
                f"file://{source_path}", name="Page source"
            ))
        extras.append(pytest_html.extras.text(
            f"URL at failure: {current_url}", name="URL"
        ))
        report.extras = extras
    except ImportError:
        pass   # pytest-html not installed — skip silently


# ── Log test start and end ─────────────────────────────────────────────────────

def pytest_runtest_logreport(report):
    if report.when == "call":
        status = "PASS" if report.passed else ("FAIL" if report.failed else "SKIP")
        logger.info(f"{status}  {report.nodeid}  ({report.duration:.2f}s)")