# =============================================================================
# tests/test_medicine_details.py
# Test cases for the Medicine Details module  (TC-MDT-01 to TC-MDT-06)
# =============================================================================

import pytest
from test_data.test_data import MedicineDetailData
from locators.locators import MedicineDetailsPage as L


class TestMedicineDetails:

    # TC-MDT-01
    def test_medicine_details_page_loads(self, medicine_details_page):
        assert medicine_details_page.is_on_page(), \
            "Should be on medicine_details.php"
        assert "Medicine" in medicine_details_page.get_heading(), \
            "Heading should contain 'Medicine'"

    # TC-MDT-02
    def test_add_medicine_detail_valid_data(self, medicine_details_page):
        medicine_details_page.add_medicine_detail(
            MedicineDetailData.MEDICINE, MedicineDetailData.PACKING
        )
        medicine_details_page.helpers.wait_for_url_contains("medicine_details.php")
        assert medicine_details_page.get_row_count() >= 1, \
            "At least one row should exist in the table after adding"

    # TC-MDT-03
    def test_form_fields_are_present(self, medicine_details_page):
        for label, locator in [
            ("Medicine Select", L.MEDICINE_SELECT),
            ("Packing Input",   L.PACKING_INPUT),
            ("Save Button",     L.SAVE_BTN),
        ]:
            assert medicine_details_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible in the form"

    # TC-MDT-04
    def test_medicine_details_table_present(self, medicine_details_page):
        assert medicine_details_page.helpers.is_displayed(L.TABLE), \
            "Medicine Details table should be visible"

    # TC-MDT-05
    def test_table_has_correct_columns(self, medicine_details_page):
        expected = ["S.No", "Medicine Name", "Packing", "Action"]
        for i, col in enumerate(expected, start=1):
            locator = ("xpath", f"//table[@id='medicine_details']//th[{i}]")
            text = medicine_details_page.helpers.get_text(locator)
            assert col.lower() in text.lower(), \
                f"Column {i} expected '{col}', got '{text}'"

    # TC-MDT-06
    def test_search_medicine_details(self, medicine_details_page):
        medicine_details_page.search(MedicineDetailData.MEDICINE)
        import time; time.sleep(0.5)
        count = medicine_details_page.get_row_count()
        assert count >= 1, \
            f"Should find at least 1 row when searching '{MedicineDetailData.MEDICINE}'"
