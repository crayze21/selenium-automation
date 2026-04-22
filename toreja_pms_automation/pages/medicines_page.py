# =============================================================================
# pages/medicines_page.py
# Page Object for the Medicines page (medicines.php)
# =============================================================================

import logging
import time
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import MedicinesPage as L, URLs

logger = logging.getLogger(__name__)


class MedicinesPage(BasePage):

    def open(self) -> "MedicinesPage":
        self.go_to(URLs.MEDICINES)
        self.wait.until(EC.presence_of_element_located(L.TABLE))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "medicines.php" in self.get_current_url()

    # ── Add Medicine form ──────────────────────────────────────────────────────

    def enter_medicine_name(self, name: str) -> "MedicinesPage":
        self.helpers.type_text(L.MEDICINE_NAME, name)
        return self

    def click_save(self) -> None:
        self.helpers.click(L.SAVE_BTN)

    def add_medicine(self, name: str) -> None:
        """Fill and submit the Add Medicine form."""
        self.enter_medicine_name(name)
        self.click_save()
        logger.info(f"Add medicine submitted: {name}")

    # ── DataTable ──────────────────────────────────────────────────────────────

    def search_medicine(self, keyword: str) -> None:
        self.helpers.search_datatable(L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return self.helpers.get_table_row_count(L.TABLE)

    def get_page_info_text(self) -> str:
        return self.helpers.get_text(L.PAGE_INFO)

    def get_cell_text(self, row: int, col: int) -> str:
        return self.helpers.get_table_cell_text("all_medicines", row, col)

    def is_medicine_in_table(self, name: str) -> bool:
        self.search_medicine(name)
        time.sleep(0.5)
        try:
            from selenium.webdriver.common.by import By
            rows = self.driver.find_elements(
                By.CSS_SELECTOR, "#all_medicines tbody tr td:nth-child(2)"
            )
            return any(name.lower() in r.text.lower() for r in rows)
        except Exception:
            return False

    def click_edit_first_row(self) -> None:
        self.helpers.click(L.ANY_EDIT_BTN)
