# =============================================================================
# pages/reports_page.py
# Page Object for the Reports page (reports.php)
# =============================================================================

import logging
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import ReportsPage as L, URLs

logger = logging.getLogger(__name__)


class ReportsPage(BasePage):

    def open(self) -> "ReportsPage":
        self.go_to(URLs.REPORTS)
        self.wait.until(EC.presence_of_element_located(L.PATIENTS_FROM))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "reports.php" in self.get_current_url()

    # ── Section 1: Patient Visits Report ──────────────────────────────────────

    def set_visits_from_date(self, date_str: str) -> "ReportsPage":
        """date_str: YYYY-MM-DD"""
        self.helpers.set_date_via_js(L.PATIENTS_FROM, date_str)
        return self

    def set_visits_to_date(self, date_str: str) -> "ReportsPage":
        self.helpers.set_date_via_js(L.PATIENTS_TO, date_str)
        return self

    def click_generate_visits_pdf(self) -> None:
        self.helpers.click(L.GENERATE_VISITS_PDF)
        logger.info("Generate Visits PDF clicked")

    def generate_visits_report(self, from_date: str, to_date: str) -> None:
        self.set_visits_from_date(from_date)
        self.set_visits_to_date(to_date)
        self.click_generate_visits_pdf()

    # ── Section 2: Disease Based Report ───────────────────────────────────────

    def enter_disease(self, disease: str) -> "ReportsPage":
        self.helpers.type_text(L.DISEASE_INPUT, disease)
        return self

    def set_disease_from_date(self, date_str: str) -> "ReportsPage":
        self.helpers.set_date_via_js(L.DISEASE_FROM, date_str)
        return self

    def set_disease_to_date(self, date_str: str) -> "ReportsPage":
        self.helpers.set_date_via_js(L.DISEASE_TO, date_str)
        return self

    def click_generate_disease_pdf(self) -> None:
        self.helpers.click(L.GENERATE_DISEASE_PDF)
        logger.info("Generate Disease PDF clicked")

    def generate_disease_report(self, disease: str, from_date: str, to_date: str) -> None:
        self.enter_disease(disease)
        self.set_disease_from_date(from_date)
        self.set_disease_to_date(to_date)
        self.click_generate_disease_pdf()

    # ── Assertions ─────────────────────────────────────────────────────────────

    def is_visits_section_displayed(self) -> bool:
        return self.helpers.is_displayed(L.VISITS_HEADING)

    def is_disease_section_displayed(self) -> bool:
        return self.helpers.is_displayed(L.DISEASE_HEADING)
