# =============================================================================
# pages/users_page.py
# Page Object for the Users page (users.php)
# =============================================================================

import logging
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import UsersPage as L, URLs

logger = logging.getLogger(__name__)


class UsersPage(BasePage):

    def open(self) -> "UsersPage":
        self.go_to(URLs.USERS)
        self.wait.until(EC.presence_of_element_located(L.TABLE))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "users.php" in self.get_current_url()

    # ── Add User form ──────────────────────────────────────────────────────────

    def enter_display_name(self, name: str) -> "UsersPage":
        self.helpers.type_text(L.DISPLAY_NAME, name)
        return self

    def enter_username(self, username: str) -> "UsersPage":
        self.helpers.type_text(L.USERNAME, username)
        return self

    def enter_password(self, password: str) -> "UsersPage":
        self.helpers.type_text(L.PASSWORD, password)
        return self

    def upload_profile_picture(self, file_path: str) -> "UsersPage":
        """Provide absolute file path to the profile picture."""
        self.driver.find_element(*L.PROFILE_PIC).send_keys(file_path)
        return self

    def click_save(self) -> None:
        self.helpers.click(L.SAVE_BTN)

    def add_user(self, display_name: str, username: str, password: str) -> None:
        """Fill and submit the Add User form."""
        self.enter_display_name(display_name)
        self.enter_username(username)
        self.enter_password(password)
        self.click_save()
        logger.info(f"Add user submitted: {username}")

    # ── Table ──────────────────────────────────────────────────────────────────

    def get_row_count(self) -> int:
        return self.helpers.get_table_row_count(L.TABLE)

    def get_cell_text(self, row: int, col: int) -> str:
        return self.helpers.get_table_cell_text("all_users", row, col)

    def click_edit_first_row(self) -> None:
        self.helpers.click(L.ANY_EDIT_BTN)
