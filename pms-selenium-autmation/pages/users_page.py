# =============================================================================
# pages/users_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import UsersPage as L, URLs
from utils.helpers import get_table_row_count


class UsersPage(BasePage):
    """Page Object for users.php."""

    def open_users_page(self) -> None:
        self.open(URLs.USERS)

    # ------------------------------------------------------------------
    # Add User form
    # ------------------------------------------------------------------

    def enter_display_name(self, name: str) -> None:
        self.type_text(L.DISPLAY_NAME_INPUT, name)

    def enter_username(self, username: str) -> None:
        self.type_text(L.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.type_text(L.PASSWORD_INPUT, password)

    def click_save_user(self) -> None:
        self.click(L.SAVE_USER_NAME)

    def add_user(self, display_name: str, username: str, password: str) -> None:
        self.enter_display_name(display_name)
        self.enter_username(username)
        self.enter_password(password)
        self.click_save_user()

    # ------------------------------------------------------------------
    # Table
    # ------------------------------------------------------------------

    def get_row_count(self) -> int:
        return get_table_row_count(self.driver, L.TABLE)

    def get_column_headers(self) -> list[str]:
        return [
            self.get_text(L.TH_SNO),
            self.get_text(L.TH_PICTURE),
            self.get_text(L.TH_DISPLAY_NAME),
            self.get_text(L.TH_USERNAME),
            self.get_text(L.TH_ACTION),
        ]