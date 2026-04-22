# =============================================================================
# tests/test_reports.py
# Test cases for the Reports module  (TC-RPT-01 to TC-RPT-06)
# =============================================================================

import pytest
from test_data.test_data import ReportData
from locators.locators import ReportsPage as L


class TestReports:

    # TC-RPT-01
    def test_reports_page_loads(self, reports_page):
        assert reports_page.is_on_page(), "Should be on reports.php"
        assert "Report" in reports_page.get_heading(), \
            "Heading should contain 'Report'"

    # TC-RPT-02
    def test_visits_section_is_visible(self, reports_page):
        assert reports_page.is_visits_section_displayed(), \
            "'Patient Visits Between Two Dates' section should be visible"

    # TC-RPT-03
    def test_disease_section_is_visible(self, reports_page):
        assert reports_page.is_disease_section_displayed(), \
            "'Disease Based Report' section should be visible"

    # TC-RPT-04
    def test_visits_form_fields_visible(self, reports_page):
        for label, locator in [
            ("From date",       L.PATIENTS_FROM),
            ("To date",         L.PATIENTS_TO),
            ("Generate PDF btn",L.GENERATE_VISITS_PDF),
        ]:
            assert reports_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible in visits report section"

    # TC-RPT-05
    def test_disease_form_fields_visible(self, reports_page):
        for label, locator in [
            ("Disease input",    L.DISEASE_INPUT),
            ("From date",        L.DISEASE_FROM),
            ("To date",          L.DISEASE_TO),
            ("Generate PDF btn", L.GENERATE_DISEASE_PDF),
        ]:
            assert reports_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible in disease report section"

    # TC-RPT-06
    def test_generate_visits_pdf_button_clickable(self, reports_page):
        reports_page.set_visits_from_date(ReportData.FROM_DATE)
        reports_page.set_visits_to_date(ReportData.TO_DATE)
        assert reports_page.helpers.is_enabled(L.GENERATE_VISITS_PDF), \
            "Generate PDF button should be enabled"

    def test_generate_disease_pdf_button_clickable(self, reports_page):
        reports_page.enter_disease(ReportData.DISEASE)
        reports_page.set_disease_from_date(ReportData.FROM_DATE)
        reports_page.set_disease_to_date(ReportData.TO_DATE)
        assert reports_page.helpers.is_enabled(L.GENERATE_DISEASE_PDF), \
            "Generate Disease PDF button should be enabled"
