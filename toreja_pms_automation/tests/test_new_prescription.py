# =============================================================================
# tests/test_new_prescription.py
# Test cases for the New Prescription module  (TC-PRX-01 to TC-PRX-10)
# =============================================================================

import pytest
from test_data.test_data import PrescriptionData
from locators.locators import NewPrescriptionPage as L


class TestNewPrescription:

    # TC-PRX-01
    def test_new_prescription_page_loads(self, new_prescription_page):
        assert new_prescription_page.is_on_page(), \
            "Should be on new_prescription.php"
        assert "Prescription" in new_prescription_page.get_heading(), \
            "Heading should mention 'Prescription'"

    # TC-PRX-02
    def test_add_row_button_adds_medicine_row(self, new_prescription_page):
        initial_count = new_prescription_page.get_row_count()
        new_prescription_page.click_add_row()
        new_count = new_prescription_page.get_row_count()
        assert new_count == initial_count + 1, \
            f"Row count should increase by 1, was {initial_count}, now {new_count}"

    # TC-PRX-03
    def test_visit_date_field_accepts_value(self, new_prescription_page):
        new_prescription_page.set_visit_date(PrescriptionData.VISIT_DATE)
        from selenium.webdriver.common.by import By
        val = new_prescription_page.driver.find_element(
            By.NAME, "visit_date"
        ).get_attribute("value")
        assert val != "", "Visit date should be set"

    # TC-PRX-04
    def test_bp_and_weight_fields_accept_input(self, new_prescription_page):
        new_prescription_page.enter_bp(PrescriptionData.BP)
        new_prescription_page.enter_weight(PrescriptionData.WEIGHT)
        assert new_prescription_page.helpers.get_value(L.BP_INPUT) == PrescriptionData.BP
        assert new_prescription_page.helpers.get_value(L.WEIGHT_INPUT) == PrescriptionData.WEIGHT

    # TC-PRX-05
    def test_disease_field_accepts_input(self, new_prescription_page):
        new_prescription_page.enter_disease(PrescriptionData.DISEASE)
        assert new_prescription_page.helpers.get_value(L.DISEASE_INPUT) == PrescriptionData.DISEASE

    # TC-PRX-06
    def test_delete_medicine_row_removes_row(self, new_prescription_page):
        new_prescription_page.click_add_row()
        count_after_add = new_prescription_page.get_row_count()
        new_prescription_page.delete_medicine_row(count_after_add)
        count_after_delete = new_prescription_page.get_row_count()
        assert count_after_delete == count_after_add - 1, \
            "Deleting a row should decrease the row count by 1"

    # TC-PRX-07
    def test_form_fields_are_present(self, new_prescription_page):
        for label, locator in [
            ("Patient Select",   L.PATIENT_SELECT),
            ("Visit Date",       L.VISIT_DATE),
            ("Next Visit Date",  L.NEXT_VISIT_DATE),
            ("BP",               L.BP_INPUT),
            ("Weight",           L.WEIGHT_INPUT),
            ("Disease",          L.DISEASE_INPUT),
            ("Add Row Button",   L.ADD_ROW_BTN),
            ("Save Button",      L.SAVE_BTN),
        ]:
            assert new_prescription_page.helpers.is_displayed(locator), \
                f"'{label}' should be visible on the prescription form"

    # TC-PRX-08
    def test_save_without_patient_stays_on_page(self, new_prescription_page):
        # Do not select a patient — go straight to save
        new_prescription_page.set_visit_date(PrescriptionData.VISIT_DATE)
        new_prescription_page.enter_disease(PrescriptionData.DISEASE)
        new_prescription_page.click_save_prescription()
        assert new_prescription_page.is_on_page(), \
            "Should remain on prescription page when no patient is selected"
