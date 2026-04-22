# =============================================================================
# tests/test_dashboard.py
# Test cases for the Dashboard module  (TC-DSH-01 to TC-DSH-07)
# =============================================================================

import pytest
from pages.dashboard_page import DashboardPage


class TestDashboard:

    # TC-DSH-01
    def test_dashboard_loads_after_login(self, dashboard_page):
        assert dashboard_page.is_on_dashboard(), "Should be on dashboard after login"
        assert "Dashboard" in dashboard_page.get_heading(), \
            "Page heading should contain 'Dashboard'"

    # TC-DSH-02
    def test_today_patients_stat_box_visible(self, dashboard_page):
        assert dashboard_page.is_today_box_displayed(), \
            "Today's Patients stat box should be visible"

    # TC-DSH-03
    def test_current_week_stat_box_visible(self, dashboard_page):
        assert dashboard_page.is_week_box_displayed(), \
            "Current Week stat box should be visible"

    # TC-DSH-04
    def test_current_month_stat_box_visible(self, dashboard_page):
        assert dashboard_page.is_month_box_displayed(), \
            "Current Month stat box should be visible"

    # TC-DSH-05
    def test_current_year_stat_box_visible(self, dashboard_page):
        assert dashboard_page.is_year_box_displayed(), \
            "Current Year stat box should be visible"

    # TC-DSH-06
    def test_stat_counts_are_numeric(self, dashboard_page):
        for label, value in [
            ("Today",   dashboard_page.get_today_count()),
            ("Week",    dashboard_page.get_week_count()),
            ("Month",   dashboard_page.get_month_count()),
            ("Year",    dashboard_page.get_year_count()),
        ]:
            assert value.isdigit(), f"{label} count should be numeric, got: '{value}'"

    # TC-DSH-07
    def test_sidebar_navigation_links_present(self, dashboard_page):
        from locators.locators import NavBar
        for label, locator in [
            ("Dashboard", NavBar.MENU_DASHBOARD_LINK),
            ("Patients",  NavBar.MENU_PATIENTS_LINK),
            ("Medicines", NavBar.MENU_MEDICINES_LINK),
            ("Reports",   NavBar.MENU_REPORTS_LINK),
            ("Users",     NavBar.MENU_USERS_LINK),
            ("Logout",    NavBar.LOGOUT_LINK),
        ]:
            assert dashboard_page.helpers.is_displayed(locator), \
                f"'{label}' link should be visible in sidebar"

    def test_footer_is_present(self, dashboard_page):
        from locators.locators import NavBar
        assert dashboard_page.helpers.is_displayed(NavBar.FOOTER), \
            "Footer should be present on dashboard"

    def test_welcome_message_contains_admin(self, dashboard_page):
        welcome = dashboard_page.get_welcome_text()
        assert "Administrator" in welcome or "Welcome" in welcome, \
            f"Welcome message should mention Administrator, got: '{welcome}'"
