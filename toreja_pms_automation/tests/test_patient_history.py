# =============================================================================
# tests/test_patient_history.py
# Test cases for the Patient History module  (TC-PHX-01 to TC-PHX-05)
# =============================================================================

import pytest
from locators.locators import PatientHistoryPage as L


class TestPatientHistory:

    # TC-PHX-01
    def test_patient_history_page_loads(self, patient_history_page):
        assert patient_history_page.is_on_page(), \
            "Should be on patient_history.php"
        assert "History" in patient_history_page.get_heading(), \
            "Heading should mention 'History'"

    # TC-PHX-02
    def test_search_section_is_visible(self, patient_history_page):
        assert patient_history_page.helpers.is_displayed(L.SECTION_HEADING), \
            "'Search Patient History' heading should be visible"
        assert patient_history_page.helpers.is_displayed(L.PATIENT_SELECT), \
            "Patient dropdown should be visible"
        assert patient_history_page.helpers.is_displayed(L.SEARCH_BTN), \
            "Search button should be visible"

    # TC-PHX-03
    def test_history_table_has_correct_columns(self, patient_history_page):
        expected = [
            "S.No", "Visit Date", "Disease", "Medicine",
            "Packing", "QTY", "Dosage", "Instruction", "Action"
        ]
        for i, col in enumerate(expected, start=1):
            locator = ("xpath", f"//table[@id='patient_history']//th[{i}]")
            text = patient_history_page.helpers.get_text(locator)
            assert col.lower() in text.lower(), \
                f"Column {i} should be '{col}', got '{text}'"

    # TC-PHX-04
    def test_search_without_selecting_patient_stays_on_page(self, patient_history_page):
        """Click Search without selecting a patient."""
        patient_history_page.click_search()
        assert patient_history_page.is_on_page(), \
            "Should remain on patient history page"

    # TC-PHX-05
    def test_history_table_is_present(self, patient_history_page):
        assert patient_history_page.helpers.is_displayed(L.TABLE), \
            "Patient history table should be present"
