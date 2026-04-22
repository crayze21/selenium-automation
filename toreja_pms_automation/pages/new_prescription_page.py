# =============================================================================
# pages/new_prescription_page.py
# Page Object for the New Prescription page (new_prescription.php)
# =============================================================================

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import NewPrescriptionPage as L, URLs

logger = logging.getLogger(__name__)


class NewPrescriptionPage(BasePage):

    def open(self) -> "NewPrescriptionPage":
        self.go_to(URLs.NEW_PRESCRIPTION)
        self.wait.until(EC.presence_of_element_located(L.VISIT_DATE))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "new_prescription.php" in self.get_current_url()

    # ── Patient Select2 dropdown ───────────────────────────────────────────────

    def select_patient(self, patient_name: str) -> "NewPrescriptionPage":
        """
        Select a patient from the Select2 dropdown.
        patient_name: partial or full name as shown in the dropdown.
        """
        self.helpers.click(L.PATIENT_S2_TRIGGER)
        time.sleep(0.3)
        self.helpers.type_text(L.PATIENT_SEARCH, patient_name, clear=False)
        time.sleep(0.5)
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class,'select2-results__option') and contains(.,'{patient_name}')]")
        ))
        option.click()
        logger.info(f"Patient selected: {patient_name}")
        return self

    # ── Visit fields ───────────────────────────────────────────────────────────

    def set_visit_date(self, date_str: str) -> "NewPrescriptionPage":
        """date_str format: YYYY-MM-DD"""
        self.helpers.set_date_via_js(L.VISIT_DATE, date_str)
        return self

    def set_next_visit_date(self, date_str: str) -> "NewPrescriptionPage":
        self.helpers.set_date_via_js(L.NEXT_VISIT_DATE, date_str)
        return self

    def enter_bp(self, bp: str) -> "NewPrescriptionPage":
        self.helpers.type_text(L.BP_INPUT, bp)
        return self

    def enter_weight(self, weight: str) -> "NewPrescriptionPage":
        self.helpers.type_text(L.WEIGHT_INPUT, weight)
        return self

    def enter_disease(self, disease: str) -> "NewPrescriptionPage":
        self.helpers.type_text(L.DISEASE_INPUT, disease)
        return self

    # ── Medicine rows ──────────────────────────────────────────────────────────

    def click_add_row(self) -> "NewPrescriptionPage":
        self.helpers.click(L.ADD_ROW_BTN)
        time.sleep(0.3)
        return self

    def get_row_count(self) -> int:
        tbody = self.driver.find_element(*L.MEDICATION_TBODY)
        return len(tbody.find_elements(By.TAG_NAME, "tr"))

    def fill_medicine_row(self, row_index: int, medicine: str,
                          frequency: str, timing: str, qty: str, dosage: str) -> None:
        """
        Fill a medicine row by its 1-based row_index.
        Selects medicine via Select2, then fills frequency/timing/qty/dosage.
        """
        tbody = self.driver.find_element(*L.MEDICATION_TBODY)
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        row = rows[row_index - 1]

        # Select medicine (Select2)
        s2_trigger = row.find_element(By.CSS_SELECTOR, ".select2-selection")
        s2_trigger.click()
        time.sleep(0.3)
        search = self.driver.find_element(*L.MEDICINE_SEARCH)
        search.send_keys(medicine)
        time.sleep(0.5)
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class,'select2-results__option') and contains(.,'{medicine}')]")
        ))
        option.click()

        # Frequency
        freq_el = row.find_elements(By.TAG_NAME, "select")[0]
        from selenium.webdriver.support.ui import Select as NativeSelect
        NativeSelect(freq_el).select_by_visible_text(frequency)

        # Timing
        timing_el = row.find_elements(By.TAG_NAME, "select")[1]
        NativeSelect(timing_el).select_by_visible_text(timing)

        # QTY
        qty_el = row.find_element(By.NAME, "qty[]")
        qty_el.clear()
        qty_el.send_keys(qty)

        # Dosage
        dosage_el = row.find_element(By.NAME, "dosage[]")
        dosage_el.clear()
        dosage_el.send_keys(dosage)

        logger.info(f"Row {row_index} filled: {medicine} | {frequency} | {timing} | {qty} | {dosage}")

    def delete_medicine_row(self, row_index: int) -> None:
        """Click the delete button on the specified row (1-based)."""
        tbody = self.driver.find_element(*L.MEDICATION_TBODY)
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        rows[row_index - 1].find_element(By.TAG_NAME, "button").click()
        time.sleep(0.2)

    # ── Submit ─────────────────────────────────────────────────────────────────

    def click_save_prescription(self) -> None:
        self.helpers.click(L.SAVE_BTN)
        logger.info("Save Prescription clicked")
