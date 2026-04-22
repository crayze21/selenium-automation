# =============================================================================
# pages/dashboard_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import DashboardPage as L, NavBar, URLs


class DashboardPage(BasePage):
    """Page Object for dashboard.php."""

    def open_dashboard(self) -> None:
        self.open(URLs.DASHBOARD)

    # ------------------------------------------------------------------
    # Stat box getters
    # ------------------------------------------------------------------

    def get_today_patients_count(self) -> str:
        return self.get_text(L.STAT_TODAY_COUNT)

    def get_current_week_count(self) -> str:
        return self.get_text(L.STAT_WEEK_COUNT)

    def get_current_month_count(self) -> str:
        return self.get_text(L.STAT_MONTH_COUNT)

    def get_current_year_count(self) -> str:
        return self.get_text(L.STAT_YEAR_COUNT)

    def is_stat_box_visible(self, locator) -> bool:
        return self.is_present(locator)

    # ------------------------------------------------------------------
    # Sidebar / navbar
    # ------------------------------------------------------------------

    def get_welcome_text(self) -> str:
        return self.get_text(NavBar.WELCOME_TEXT)

    def is_sidebar_visible(self) -> bool:
        return self.is_present(NavBar.SIDEBAR)

    def get_footer_text(self) -> str:
        return self.get_text(NavBar.FOOTER)

    # ------------------------------------------------------------------
    # Navigation helpers
    # ------------------------------------------------------------------

    def navigate_to_patients(self) -> None:
        self.click(NavBar.MENU_PATIENTS_LINK)
        self.click(NavBar.SUBMENU_PATIENTS)

    def navigate_to_new_prescription(self) -> None:
        self.click(NavBar.MENU_PATIENTS_LINK)
        self.click(NavBar.SUBMENU_NEW_PRESCRIPTION)

    def navigate_to_patient_history(self) -> None:
        self.click(NavBar.MENU_PATIENTS_LINK)
        self.click(NavBar.SUBMENU_PATIENT_HISTORY)

    def navigate_to_medicines(self) -> None:
        self.click(NavBar.MENU_MEDICINES_LINK)
        self.click(NavBar.SUBMENU_ADD_MEDICINE)

    def navigate_to_medicine_details(self) -> None:
        self.click(NavBar.MENU_MEDICINES_LINK)
        self.click(NavBar.SUBMENU_MEDICINE_DETAILS)

    def navigate_to_reports(self) -> None:
        self.click(NavBar.MENU_REPORTS_LINK)
        self.click(NavBar.SUBMENU_REPORTS)

    def navigate_to_users(self) -> None:
        self.click(NavBar.MENU_USERS_LINK)

    def logout(self) -> None:
        self.click(NavBar.LOGOUT_LINK)