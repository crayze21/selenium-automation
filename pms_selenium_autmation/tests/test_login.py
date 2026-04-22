# =============================================================================
# tests/test_login.py
# Test cases: TC-LGN-01 through TC-LGN-08
# =============================================================================

import pytest
from pages.login_page import LoginPage
from locators.locators import URLs


@pytest.mark.login
class TestLogin:
    """3.1 Login Module — 8 test cases."""

    # TC-LGN-01 ----------------------------------------------------------------
    def test_valid_login(self, driver):
        """Valid credentials → redirected to dashboard."""
        pass  # TODO: implement

    # TC-LGN-02 ----------------------------------------------------------------
    def test_invalid_username(self, driver):
        """Wrong username → error message shown, stays on login page."""
        pass  # TODO: implement

    # TC-LGN-03 ----------------------------------------------------------------
    def test_invalid_password(self, driver):
        """Wrong password → 'Incorrect username or password.' shown."""
        pass  # TODO: implement

    # TC-LGN-04 ----------------------------------------------------------------
    def test_empty_username(self, driver):
        """Blank username → form not submitted, stays on login page."""
        pass  # TODO: implement

    # TC-LGN-05 ----------------------------------------------------------------
    def test_empty_password(self, driver):
        """Blank password → form not submitted."""
        pass  # TODO: implement

    # TC-LGN-06 ----------------------------------------------------------------
    @pytest.mark.smoke
    def test_both_fields_empty(self, driver):
        """Both blank → appropriate error or form not submitted."""
        pass  # TODO: implement

    # TC-LGN-07 ----------------------------------------------------------------
    def test_logout_functionality(self, logged_in_driver):
        """Logout → redirected to login page, session cleared."""
        pass  # TODO: implement

    # TC-LGN-08 ----------------------------------------------------------------
    def test_page_title_on_login(self, driver):
        """Login page title is 'Toreja Medical Clinic'."""
        pass  # TODO: implement