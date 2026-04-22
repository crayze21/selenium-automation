# =============================================================================
# pages/patient_history_page.py
# Page Object for the Patient History page (patient_history.php)
# =============================================================================

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import PatientHistoryPage as L, URLs

logger = logging.getLogger(__name__)


class PatientHistoryPage(BasePage):

    def open(self) -> "PatientHistoryPage":
        self.go_to(URLs.PATIENT_HISTORY)
        self.wait.until(EC.presence_of_element_located(L.SEARCH_BTN))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "patient_history.php" in self.get_current_url()

    # ── Search ─────────────────────────────────────────────────────────────────

    def select_patient(self, patient_name: str) -> "PatientHistoryPage":
        """Select a patient from the Select2 dropdown."""
        self.helpers.click(L.PATIENT_S2_TRIGGER)
        time.sleep(0.3)
        self.helpers.type_text(L.PATIENT_SEARCH, patient_name, clear=False)
        time.sleep(0.5)
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class,'select2-results__option') and contains(.,'{patient_name}')]")
        ))
        option.click()
        logger.info(f"Patient selected for history search: {patient_name}")
        return self

    def click_search(self) -> None:
        self.helpers.click(L.SEARCH_BTN)
        time.sleep(0.8)

    def search_patient_history(self, patient_name: str) -> None:
        """Select a patient and click Search."""
        self.select_patient(patient_name)
        self.click_search()

    # ── Results ────────────────────────────────────────────────────────────────

    def get_result_row_count(self) -> int:
        tbody = self.driver.find_element(*L.HISTORY_TBODY)
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        return len([r for r in rows if r.text.strip()])

    def is_table_empty(self) -> bool:
        return self.get_result_row_count() == 0

    def get_cell_text(self, row: int, col: int) -> str:
        return self.helpers.get_table_cell_text("patient_history", row, col)
