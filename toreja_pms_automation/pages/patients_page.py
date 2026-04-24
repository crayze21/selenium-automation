# =============================================================================
# pages/patients_page.py
# Page Object for the Patients page (patients.php)
# =============================================================================

import logging
import time
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger
from utils.test_step import step
from pages.base_page import BasePage
from locators.locators import PatientsPage as L, URLs

logger = logging.getLogger(__name__)


class PatientsPage(BasePage):

    def open(self) -> "PatientsPage":
        self.go_to(URLs.PATIENTS)
        self.wait.until(EC.presence_of_element_located(L.TABLE))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "patients.php" in self.get_current_url()

    # ── Add Patient form ───────────────────────────────────────────────────────

    def enter_patient_name(self, name: str) -> "PatientsPage":
        self.helpers.type_text(L.PATIENT_NAME, name)
        return self

    def enter_address(self, address: str) -> "PatientsPage":
        self.helpers.type_text(L.ADDRESS, address)
        return self

    def enter_cnic(self, cnic: str) -> "PatientsPage":
        self.helpers.type_text(L.CNIC, cnic)
        return self

    def enter_date_of_birth(self, dob: str) -> "PatientsPage":
        """Set date of birth via JavaScript to bypass custom date picker. Format: YYYY-MM-DD"""
        self.helpers.set_date_via_js(L.DATE_OF_BIRTH_INPUT, dob)
        return self

    def enter_phone_number(self, phone: str) -> "PatientsPage":
        self.helpers.type_text(L.PHONE_NUMBER, phone)
        return self

    def select_gender(self, gender: str) -> "PatientsPage":
        """Select gender: 'Male', 'Female', or 'Other'"""
        self.helpers.select_by_visible_text(L.GENDER, gender)
        return self

    def click_save(self) -> None:
        self.helpers.click(L.SAVE_BTN)

    def add_patient(self, name: str, address: str, cnic: str,
                    dob: str, phone: str, gender: str) -> None:
        """Fill and submit the Add Patient form."""
        logger.info(f"Add patient submitted: {name}")
        with step("Enter patient name"):
            self.helpers.type_text(L.PATIENT_NAME, name)
        with step("Enter address"):
            self.helpers.type_text(L.ADDRESS, address)
        with step("Enter CNIC"):
            self.helpers.type_text(L.CNIC, cnic)
        with step("Set date of birth"):
            self.helpers.set_date_via_js(L.DATE_OF_BIRTH_INPUT, dob)
        with step("Enter phone number"):
            self.helpers.type_text(L.PHONE_NUMBER, phone)
        with step("Select gender"):
            self.helpers.select_by_visible_text(L.GENDER, gender)
        with step("Click Save button"):
            self.helpers.click(L.SAVE_BTN)

    # ── DataTable interactions ─────────────────────────────────────────────────

    def search_patient(self, keyword: str) -> None:
        self.helpers.search_datatable(L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return self.helpers.get_table_row_count(L.TABLE)

    def get_page_info_text(self) -> str:
        return self.helpers.get_text(L.PAGE_INFO)

    def click_edit_first_row(self) -> None:
        self.helpers.click(L.ANY_EDIT_BTN)

    def get_cell_text(self, row: int, col: int) -> str:
        return self.helpers.get_table_cell_text("all_patients", row, col)

    def is_patient_in_table(self, name: str) -> bool:
        """Search for patient by name and check they appear in results."""
        self.search_patient(name)
        time.sleep(0.5)
        try:
            from selenium.webdriver.common.by import By
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#all_patients tbody tr td:nth-child(2)")
            return any(name.lower() in r.text.lower() for r in rows)
        except Exception:
            return False

    # ── Export buttons ─────────────────────────────────────────────────────────

    def click_export_csv(self) -> None:
        self.helpers.click(L.BTN_CSV)

    def click_export_excel(self) -> None:
        self.helpers.click(L.BTN_EXCEL)

    def click_export_pdf(self) -> None:
        self.helpers.click(L.BTN_PDF)

    def click_print(self) -> None:
        self.helpers.click(L.BTN_PRINT)
