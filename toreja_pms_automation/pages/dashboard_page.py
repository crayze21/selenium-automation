# =============================================================================
# pages/dashboard_page.py
# Page Object for the Dashboard page (dashboard.php)
# =============================================================================

import logging
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import DashboardPage as L, URLs

logger = logging.getLogger(__name__)


class DashboardPage(BasePage):

    def open(self) -> "DashboardPage":
        self.go_to(URLs.DASHBOARD)
        self.wait.until(EC.presence_of_element_located(L.PAGE_HEADING))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_dashboard(self) -> bool:
        return "dashboard.php" in self.get_current_url()

    # ── Stat box values ────────────────────────────────────────────────────────

    def get_today_count(self) -> str:
        return self.helpers.get_text(L.COUNT_TODAY)

    def get_week_count(self) -> str:
        return self.helpers.get_text(L.COUNT_WEEK)

    def get_month_count(self) -> str:
        return self.helpers.get_text(L.COUNT_MONTH)

    def get_year_count(self) -> str:
        return self.helpers.get_text(L.COUNT_YEAR)

    def is_today_box_displayed(self) -> bool:
        return self.helpers.is_displayed(L.BOX_TODAY)

    def is_week_box_displayed(self) -> bool:
        return self.helpers.is_displayed(L.BOX_WEEK)

    def is_month_box_displayed(self) -> bool:
        return self.helpers.is_displayed(L.BOX_MONTH)

    def is_year_box_displayed(self) -> bool:
        return self.helpers.is_displayed(L.BOX_YEAR)
