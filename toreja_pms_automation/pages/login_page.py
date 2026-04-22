# =============================================================================
# pages/login_page.py
# Page Object for the Login page (index.php)
# =============================================================================

import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.locators import LoginPage as L, URLs

logger = logging.getLogger(__name__)


class LoginPage(BasePage):

    def open(self) -> "LoginPage":
        """Navigate to the login page."""
        self.go_to(URLs.LOGIN)
        self.wait.until(EC.presence_of_element_located(L.USERNAME_INPUT))
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.helpers.type_text(L.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.helpers.type_text(L.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        self.helpers.click(L.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Complete login flow with given credentials."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        logger.info(f"Login attempted with username: '{username}'")

    def login_as_admin(self) -> None:
        """Log in using credentials from Config."""
        from utils.config import Config
        self.login(Config.USERNAME, Config.PASSWORD)

    def get_error_message(self) -> str:
        """Return the error message text if login fails."""
        try:
            return self.helpers.get_text(L.ERROR_MESSAGE)
        except Exception:
            return ""

    def is_error_displayed(self) -> bool:
        return self.helpers.is_displayed(L.ERROR_MESSAGE)

    def is_on_login_page(self) -> bool:
        return "index.php" in self.get_current_url() or self.get_current_url().endswith("/")

    def is_logo_displayed(self) -> bool:
        return self.helpers.is_displayed(L.LOGO)
