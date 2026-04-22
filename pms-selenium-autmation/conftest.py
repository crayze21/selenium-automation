# =============================================================================
# conftest.py
# pytest fixtures shared across all test modules.
# =============================================================================

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import DriverFactory
from locators.locators import URLs, LoginPage


# ---------------------------------------------------------------------------
# Base driver fixture  (one browser per test function)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def driver():
    """
    Yield a fresh Chrome WebDriver for each test.
    The browser is closed automatically after the test finishes.

    To run headless (e.g. in CI) set the env var HEADLESS=1:
        HEADLESS=1 pytest
    """
    import os
    headless = os.getenv("HEADLESS", "0") == "1"
    chrome = DriverFactory.get_driver(headless=headless)
    yield chrome
    chrome.quit()


# ---------------------------------------------------------------------------
# Pre-authenticated driver fixture
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Yield a Chrome WebDriver that is already logged in as admin.
    Use this fixture in every test that requires an authenticated session.
    """
    driver.get(URLs.LOGIN)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(LoginPage.USERNAME_INPUT))
    driver.find_element(*LoginPage.USERNAME_INPUT).send_keys("admin")
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys("admin123")
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    wait.until(EC.url_contains("dashboard.php"))
    return driver