# =============================================================================
# pages/patients_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import PatientsPage as L, URLs
from utils.helpers import datatable_search, get_table_row_count, select_by_visible_text


class PatientsPage(BasePage):
    """Page Object for patients.php."""

    def open_patients_page(self) -> None:
        self.open(URLs.PATIENTS)

    # ------------------------------------------------------------------
    # Add Patient form
    # ------------------------------------------------------------------

    def enter_patient_name(self, name: str) -> None:
        self.type_text(L.PATIENT_NAME_INPUT, name)

    def enter_address(self, address: str) -> None:
        self.type_text(L.ADDRESS_INPUT, address)

    def enter_cnic(self, cnic: str) -> None:
        self.type_text(L.CNIC_INPUT, cnic)

    def enter_date_of_birth(self, dob: str) -> None:
        """Enter DOB in the date picker via JS to avoid browser date-picker quirks."""
        field = self.find(L.DATE_OF_BIRTH_INPUT)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, dob
        )

    def enter_phone_number(self, phone: str) -> None:
        self.type_text(L.PHONE_NUMBER_INPUT, phone)

    def select_gender(self, gender: str) -> None:
        select_by_visible_text(self.driver, L.GENDER_SELECT, gender)

    def click_save_patient(self) -> None:
        self.click(L.SAVE_PATIENT_BTN)

    def add_patient(
        self,
        name: str,
        address: str,
        cnic: str,
        dob: str,
        phone: str,
        gender: str,
    ) -> None:
        """Fill all Add Patient fields and submit."""
        self.enter_patient_name(name)
        self.enter_address(address)
        self.enter_cnic(cnic)
        self.enter_date_of_birth(dob)
        self.enter_phone_number(phone)
        self.select_gender(gender)
        self.click_save_patient()

    # ------------------------------------------------------------------
    # Table / search
    # ------------------------------------------------------------------

    def search_patient(self, keyword: str) -> None:
        datatable_search(self.driver, L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return get_table_row_count(self.driver, L.TABLE)

    def get_page_info_text(self) -> str:
        return self.get_text(L.PAGE_INFO)

    # ------------------------------------------------------------------
    # Export buttons
    # ------------------------------------------------------------------

    def click_csv_export(self) -> None:
        self.click(L.CSV_BTN)

    def click_copy_export(self) -> None:
        self.click(L.COPY_BTN)

    # ------------------------------------------------------------------
    # Column headers
    # ------------------------------------------------------------------

    def get_column_headers(self) -> list[str]:
        headers = [
            L.TH_SNO, L.TH_PATIENT_NAME, L.TH_ADDRESS,
            L.TH_CNIC, L.TH_DOB, L.TH_PHONE, L.TH_GENDER, L.TH_ACTION,
        ]
        return [self.get_text(h) for h in headers]

    def click_patient_name_header(self) -> None:
        self.click(L.TH_PATIENT_NAME)