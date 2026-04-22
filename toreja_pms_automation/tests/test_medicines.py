# =============================================================================
# tests/test_medicines.py
# Test cases for the Medicines module  (TC-MED-01 to TC-MED-07)
# =============================================================================

import pytest
from test_data.test_data import MedicineData
from locators.locators import MedicinesPage as L


class TestMedicines:

    # TC-MED-01
    def test_medicines_page_loads(self, medicines_page):
        assert medicines_page.is_on_page(), "Should be on medicines.php"
        assert "Medicine" in medicines_page.get_heading(), \
            "Heading should mention 'Medicine'"

    # TC-MED-02
    def test_add_medicine_valid_name(self, medicines_page):
        medicines_page.add_medicine(MedicineData.VALID_NAME)
        medicines_page.helpers.wait_for_url_contains("medicines.php")
        assert medicines_page.is_medicine_in_table(MedicineData.VALID_NAME), \
            f"Medicine '{MedicineData.VALID_NAME}' should appear in table"

    # TC-MED-03
    def test_add_medicine_empty_name_stays_on_page(self, medicines_page):
        medicines_page.add_medicine(MedicineData.EMPTY_NAME)
        assert medicines_page.is_on_page(), \
            "Should remain on medicines page with empty name"

    # TC-MED-04
    def test_medicines_table_has_correct_columns(self, medicines_page):
        expected = ["S.No", "Medicine Name", "Action"]
        for i, col in enumerate(expected, start=1):
            locator = ("xpath", f"//table[@id='all_medicines']//th[{i}]")
            text = medicines_page.helpers.get_text(locator)
            assert col.lower() in text.lower(), \
                f"Column {i} expected '{col}', got '{text}'"

    # TC-MED-05
    def test_search_filters_medicines(self, medicines_page):
        medicines_page.search_medicine(MedicineData.EXISTING)
        assert medicines_page.is_medicine_in_table(MedicineData.EXISTING), \
            f"Searching '{MedicineData.EXISTING}' should show matching result"

    # TC-MED-06
    def test_add_medicine_form_fields_visible(self, medicines_page):
        assert medicines_page.helpers.is_displayed(L.MEDICINE_NAME), \
            "Medicine Name input should be visible"
        assert medicines_page.helpers.is_displayed(L.SAVE_BTN), \
            "Save button should be visible"

    # TC-MED-07
    def test_page_info_text_is_displayed(self, medicines_page):
        info = medicines_page.get_page_info_text()
        assert "entries" in info.lower() or "Showing" in info, \
            f"Page info should show count, got: '{info}'"

    def test_export_buttons_are_visible(self, medicines_page):
        for label, locator in [
            ("Copy",  L.BTN_COPY),
            ("CSV",   L.BTN_CSV),
            ("Excel", L.BTN_EXCEL),
            ("PDF",   L.BTN_PDF),
            ("Print", L.BTN_PRINT),
        ]:
            assert medicines_page.helpers.is_displayed(locator), \
                f"'{label}' button should be visible"
