# =============================================================================
# pages/login_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import LoginPage as L, URLs


class LoginPage(BasePage):
    """Page Object for index.php (login screen)."""

    def open_login_page(self) -> None:
        self.open(URLs.LOGIN)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def enter_username(self, username: str) -> None:
        self.type_text(L.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.type_text(L.PASSWORD_INPUT, password)

    def click_sign_in(self) -> None:
        self.click(L.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Convenience: fill both fields and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()

    # ------------------------------------------------------------------
    # Getters / state
    # ------------------------------------------------------------------

    def get_error_message(self) -> str:
        return self.get_text(L.ERROR_MESSAGE)

    def get_page_title_text(self) -> str:
        return self.get_text(L.PAGE_TITLE_TEXT)

    def is_on_login_page(self) -> bool:
        return "index.php" in self.current_url or self.current_url.rstrip("/") == URLs.BASE