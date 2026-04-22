# =============================================================================
# tests/test_patients.py
# Test cases for the Patients module  (TC-PAT-01 to TC-PAT-09)
# =============================================================================

import pytest
from test_data.test_data import PatientData


class TestPatients:

    # TC-PAT-01
    def test_patients_page_loads(self, patients_page):
        assert patients_page.is_on_page(), "Should be on patients.php"
        assert "Patient" in patients_page.get_heading(), \
            "Page heading should contain 'Patient'"

    # TC-PAT-02
    def test_add_patient_valid_data(self, patients_page):
        d = PatientData.VALID
        initial_count = patients_page.get_row_count()
        patients_page.add_patient(
            d["name"], d["address"], d["cnic"],
            d["dob"],  d["phone"],  d["gender"]
        )
        patients_page.helpers.wait_for_url_contains("patients.php")
        assert patients_page.is_patient_in_table(d["name"]), \
            f"Patient '{d['name']}' should appear in table after adding"

    # TC-PAT-03
    def test_add_patient_empty_name_stays_on_page(self, patients_page):
        d = PatientData.NO_NAME
        patients_page.add_patient(
            d["name"], d["address"], d["cnic"],
            d["dob"],  d["phone"],  d["gender"]
        )
        assert patients_page.is_on_page(), \
            "Should remain on patients page when name is empty"

    # TC-PAT-04
    def test_patients_table_has_correct_columns(self, patients_page):
        from locators.locators import PatientsPage as L
        expected_headers = ["S.No", "Patient Name", "Address", "CNIC",
                            "Date Of Birth", "Phone Number", "Gender", "Action"]
        for i, expected in enumerate(expected_headers, start=1):
            locator = (L.TH_SNO[0], f"//table[@id='all_patients']//th[{i}]")
            header_text = patients_page.helpers.get_text(
                (locator[0], locator[1])
            )
            assert expected.lower() in header_text.lower(), \
                f"Column {i} should be '{expected}', got '{header_text}'"

    # TC-PAT-05
    def test_search_filters_patients(self, patients_page):
        patients_page.search_patient(PatientData.EXISTING_NAME)
        assert patients_page.is_patient_in_table(PatientData.EXISTING_NAME), \
            f"Searching '{PatientData.EXISTING_NAME}' should show matching results"

    # TC-PAT-06
    def test_search_with_no_match_shows_zero_rows(self, patients_page):
        patients_page.search_patient("ZZZNOMATCH999")
        count = patients_page.get_row_count()
        assert count == 0, f"No rows expected for non-matching search, got {count}"

    # TC-PAT-07
    def test_page_info_text_is_displayed(self, patients_page):
        info = patients_page.get_page_info_text()
        assert "entries" in info.lower() or "Showing" in info, \
            f"Page info should show entry count, got: '{info}'"

    # TC-PAT-08
    def test_export_buttons_are_visible(self, patients_page):
        from locators.locators import PatientsPage as L
        for label, locator in [
            ("Copy",   L.BTN_COPY),
            ("CSV",    L.BTN_CSV),
            ("Excel",  L.BTN_EXCEL),
            ("PDF",    L.BTN_PDF),
            ("Print",  L.BTN_PRINT),
        ]:
            assert patients_page.helpers.is_displayed(locator), \
                f"'{label}' export button should be visible"

    # TC-PAT-09
    def test_add_patients_form_fields_present(self, patients_page):
        from locators.locators import PatientsPage as L
        for label, locator in [
            ("Patient Name",  L.PATIENT_NAME),
            ("Address",       L.ADDRESS),
            ("CNIC",          L.CNIC),
            ("Phone Number",  L.PHONE_NUMBER),
            ("Gender",        L.GENDER),
            ("Save Button",   L.SAVE_BTN),
        ]:
            assert patients_page.helpers.is_displayed(locator), \
                f"'{label}' field should be visible in the Add Patients form"
