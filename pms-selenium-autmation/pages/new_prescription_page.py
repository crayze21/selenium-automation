# =============================================================================
# pages/new_prescription_page.py
# =============================================================================

import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import NewPrescriptionPage as L, URLs
from utils.helpers import select_by_visible_text, wait_for_clickable


class NewPrescriptionPage(BasePage):
    """Page Object for new_prescription.php."""

    def open_new_prescription_page(self) -> None:
        self.open(URLs.NEW_PRESCRIPTION)

    # ------------------------------------------------------------------
    # Patient Select2 dropdown
    # ------------------------------------------------------------------

    def select_patient(self, patient_name: str) -> None:
        """Open the Select2 patient dropdown, search, and pick a match."""
        # Click the Select2 trigger (the visible span wrapping the hidden select)
        trigger = (By.CSS_SELECTOR, "#select2-patient-container")
        wait_for_clickable(self.driver, trigger).click()
        time.sleep(0.3)
        search_box = self.find_visible(L.PATIENT_SEARCH_CSS)
        search_box.send_keys(patient_name)
        time.sleep(0.7)
        option = (
            By.XPATH,
            f"//li[contains(@class,'select2-results__option') "
            f"and contains(text(),'{patient_name}')]",
        )
        wait_for_clickable(self.driver, option).click()

    # ------------------------------------------------------------------
    # Visit fields
    # ------------------------------------------------------------------

    def enter_visit_date(self, date_str: str) -> None:
        field = self.find(L.VISIT_DATE)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", field, date_str
        )

    def enter_bp(self, bp: str) -> None:
        self.type_text(L.BP_INPUT, bp)

    def enter_weight(self, weight: str) -> None:
        self.type_text(L.WEIGHT_INPUT, weight)

    def enter_disease(self, disease: str) -> None:
        self.type_text(L.DISEASE_INPUT, disease)

    # ------------------------------------------------------------------
    # Medicine table rows
    # ------------------------------------------------------------------

    def click_add_row(self) -> None:
        self.click(L.ADD_ROW_BUTTON)
        time.sleep(0.3)

    def fill_medicine_row(
        self,
        row_index: int = 1,
        medicine_name: str = "",
        frequency: str = "",
        timing: str = "",
        qty: str = "",
        dosage: str = "",
    ) -> None:
        """
        Fill one medicine row in the prescription table.
        `row_index` is 1-based (first row = 1).
        """
        if medicine_name:
            search_css = (
                By.CSS_SELECTOR,
                f"#medication_list tr:nth-child({row_index}) "
                "input[placeholder='Type Medicine...']",
            )
            search_box = self.find_visible(search_css)
            search_box.send_keys(medicine_name)
            time.sleep(0.7)
            option = (
                By.XPATH,
                f"//li[contains(@class,'select2-results__option') "
                f"and contains(text(),'{medicine_name}')]",
            )
            wait_for_clickable(self.driver, option).click()

        if frequency:
            freq_locator = (
                By.XPATH,
                f"(//select[@name='frequency[]'])[{row_index}]",
            )
            select_by_visible_text(self.driver, freq_locator, frequency)

        if timing:
            timing_locator = (
                By.XPATH,
                f"(//select[@name='timing[]'])[{row_index}]",
            )
            select_by_visible_text(self.driver, timing_locator, timing)

        if qty:
            qty_locator = (By.XPATH, f"(//input[@name='qty[]'])[{row_index}]")
            self.type_text(qty_locator, qty)

        if dosage:
            dosage_locator = (By.XPATH, f"(//input[@name='dosage[]'])[{row_index}]")
            self.type_text(dosage_locator, dosage)

    def click_delete_row(self, row_index: int = 1) -> None:
        delete_btn = (
            By.XPATH,
            f"(//button[contains(@class,'btn-danger')])[{row_index}]",
        )
        self.click(delete_btn)

    def get_row_count(self) -> int:
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#medication_list tr")
        return len(rows)

    # ------------------------------------------------------------------
    # Submit
    # ------------------------------------------------------------------

    def click_save_prescription(self) -> None:
        self.click(L.SAVE_PRESCRIPTION_BTN)