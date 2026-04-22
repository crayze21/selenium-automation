# =============================================================================
# tests/test_users.py
# Test cases for the Users module  (TC-USR-01 to TC-USR-06)
# =============================================================================

import pytest
from test_data.test_data import UserData
from locators.locators import UsersPage as L


class TestUsers:

    # TC-USR-01
    def test_users_page_loads(self, users_page):
        assert users_page.is_on_page(), "Should be on users.php"
        assert "User" in users_page.get_heading(), \
            "Heading should contain 'User'"

    # TC-USR-02
    def test_add_user_form_fields_visible(self, users_page):
        for label, locator in [
            ("Display Name", L.DISPLAY_NAME),
            ("Username",     L.USERNAME),
            ("Password",     L.PASSWORD),
            ("Profile Pic",  L.PROFILE_PIC),
            ("Save Button",  L.SAVE_BTN),
        ]:
            assert users_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible in the Add User form"

    # TC-USR-03
    def test_add_user_valid_data(self, users_page):
        d = UserData.VALID
        users_page.add_user(d["display_name"], d["username"], d["password"])
        users_page.helpers.wait_for_url_contains("users.php")
        count = users_page.get_row_count()
        assert count >= 1, "At least one row should be in the users table"

    # TC-USR-04
    def test_add_user_empty_username_stays_on_page(self, users_page):
        d = UserData.EMPTY_USERNAME
        users_page.add_user(d["display_name"], d["username"], d["password"])
        assert users_page.is_on_page(), \
            "Should remain on users page when username is empty"

    # TC-USR-05
    def test_add_user_empty_password_stays_on_page(self, users_page):
        d = UserData.EMPTY_PASSWORD
        users_page.add_user(d["display_name"], d["username"], d["password"])
        assert users_page.is_on_page(), \
            "Should remain on users page when password is empty"

    # TC-USR-06
    def test_users_table_has_correct_columns(self, users_page):
        expected = ["S.No", "Picture", "Display Name", "Username", "Action"]
        for i, col in enumerate(expected, start=1):
            locator = ("xpath", f"//table[@id='all_users']//th[{i}]")
            text = users_page.helpers.get_text(locator)
            assert col.lower() in text.lower(), \
                f"Column {i} expected '{col}', got '{text}'"

    def test_all_users_table_heading_visible(self, users_page):
        assert users_page.helpers.is_displayed(L.TABLE_HEADING), \
            "'All Users' heading should be visible"
