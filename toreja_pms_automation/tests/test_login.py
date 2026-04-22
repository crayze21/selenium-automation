# =============================================================================
# tests/test_login.py
# Test cases for the Login module  (TC-LGN-01 to TC-LGN-08)
# =============================================================================

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from locators.locators import URLs
from test_data.test_data import LoginData
from utils.config import Config


class TestLogin:

    # TC-LGN-01
    def test_valid_login_redirects_to_dashboard(self, login_page):
        login_page.open()
        login_page.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        WebDriverWait(login_page.driver, Config.EXPLICIT_WAIT).until(
            EC.url_contains("dashboard.php")
        )
        assert "dashboard.php" in login_page.get_current_url(), \
            "Should redirect to dashboard after valid login"

    # TC-LGN-02
    def test_invalid_username_shows_error(self, login_page):
        login_page.open()
        login_page.login(LoginData.INVALID_USERNAME, LoginData.VALID_PASSWORD)
        assert login_page.is_on_login_page(), "Should remain on login page"
        error = login_page.get_error_message()
        assert "incorrect" in error.lower() or "invalid" in error.lower() or error != "", \
            f"Expected error message, got: '{error}'"

    # TC-LGN-03
    def test_invalid_password_shows_error(self, login_page):
        login_page.open()
        login_page.login(LoginData.VALID_USERNAME, LoginData.INVALID_PASSWORD)
        assert login_page.is_on_login_page(), "Should remain on login page"

    # TC-LGN-04
    def test_empty_username_does_not_login(self, login_page):
        login_page.open()
        login_page.login(LoginData.EMPTY, LoginData.VALID_PASSWORD)
        assert login_page.is_on_login_page(), "Should remain on login page with empty username"

    # TC-LGN-05
    def test_empty_password_does_not_login(self, login_page):
        login_page.open()
        login_page.login(LoginData.VALID_USERNAME, LoginData.EMPTY)
        assert login_page.is_on_login_page(), "Should remain on login page with empty password"

    # TC-LGN-06
    def test_both_fields_empty_does_not_login(self, login_page):
        login_page.open()
        login_page.login(LoginData.EMPTY, LoginData.EMPTY)
        assert login_page.is_on_login_page(), "Should remain on login page when both fields are empty"

    # TC-LGN-07
    def test_logout_clears_session(self, driver):
        lp = LoginPage(driver)
        lp.open()
        lp.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        WebDriverWait(driver, Config.EXPLICIT_WAIT).until(EC.url_contains("dashboard.php"))
        lp.logout()
        assert lp.is_on_login_page(), "Should be back on login page after logout"
        # Accessing dashboard should redirect back to login
        driver.get(URLs.DASHBOARD)
        WebDriverWait(driver, 5).until(EC.url_contains("index.php"))
        assert lp.is_on_login_page(), "Accessing dashboard after logout should redirect to login"

    # TC-LGN-08
    def test_page_title_on_login(self, login_page):
        login_page.open()
        assert "Toreja" in login_page.get_page_title() or \
               "Clinic" in login_page.get_page_title(), \
               "Page title should contain clinic name"

    def test_logo_is_displayed_on_login(self, login_page):
        login_page.open()
        assert login_page.is_logo_displayed(), "Clinic logo should be visible on login page"
