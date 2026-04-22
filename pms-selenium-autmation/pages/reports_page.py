# =============================================================================
# pages/reports_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import ReportsPage as L, URLs


class ReportsPage(BasePage):
    """Page Object for reports.php."""

    def open_reports_page(self) -> None:
        self.open(URLs.REPORTS)

    # ------------------------------------------------------------------
    # Section 1 – Patient Visits Report
    # ------------------------------------------------------------------

    def enter_visits_from_date(self, date_str: str) -> None:
        field = self.find(L.PATIENTS_FROM_INPUT)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, date_str
        )

    def enter_visits_to_date(self, date_str: str) -> None:
        field = self.find(L.PATIENTS_TO_INPUT)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, date_str
        )

    def click_generate_visits_pdf(self) -> None:
        self.click(L.GENERATE_VISITS_PDF_BTN)

    # ------------------------------------------------------------------
    # Section 2 – Disease Based Report
    # ------------------------------------------------------------------

    def enter_disease(self, disease: str) -> None:
        self.type_text(L.DISEASE_INPUT, disease)

    def enter_disease_from_date(self, date_str: str) -> None:
        field = self.find(L.DISEASE_FROM_INPUT)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, date_str
        )

    def enter_disease_to_date(self, date_str: str) -> None:
        field = self.find(L.DISEASE_TO_INPUT)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, date_str
        )

    def click_generate_disease_pdf(self) -> None:
        self.click(L.GENERATE_DISEASE_PDF_BTN)

    # ------------------------------------------------------------------
    # Section visibility
    # ------------------------------------------------------------------

    def is_visits_section_visible(self) -> bool:
        return self.is_present(L.VISITS_SECTION_HEADER)

    def is_disease_section_visible(self) -> bool:
        return self.is_present(L.DISEASE_SECTION_HEADER)