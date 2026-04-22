# =============================================================================
# pages/patient_history_page.py
# =============================================================================

import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import PatientHistoryPage as L, URLs
from utils.helpers import wait_for_clickable, get_table_row_count


class PatientHistoryPage(BasePage):
    """Page Object for patient_history.php."""

    def open_patient_history_page(self) -> None:
        self.open(URLs.PATIENT_HISTORY)

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def select_patient(self, patient_name: str) -> None:
        """Open the Select2 patient dropdown and choose a patient."""
        trigger = (By.CSS_SELECTOR, "#select2-patient-container")
        wait_for_clickable(self.driver, trigger).click()
        time.sleep(0.3)
        search_box = self.find_visible(L.PATIENT_SEARCH_BOX)
        search_box.send_keys(patient_name)
        time.sleep(0.7)
        option = (
            By.XPATH,
            f"//li[contains(@class,'select2-results__option') "
            f"and contains(text(),'{patient_name}')]",
        )
        wait_for_clickable(self.driver, option).click()

    def click_search(self) -> None:
        self.click(L.SEARCH_BTN)
        time.sleep(0.5)

    # ------------------------------------------------------------------
    # Table
    # ------------------------------------------------------------------

    def get_history_row_count(self) -> int:
        return get_table_row_count(self.driver, L.TABLE)

    def get_column_headers(self) -> list[str]:
        headers = [
            L.TH_SNO, L.TH_VISIT_DATE, L.TH_DISEASE,
            L.TH_MEDICINE, L.TH_PACKING, L.TH_QTY,
            L.TH_DOSAGE, L.TH_INSTRUCTION, L.TH_ACTION,
        ]
        return [self.get_text(h) for h in headers]