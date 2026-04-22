# =============================================================================
# pages/medicine_details_page.py
# Page Object for the Medicine Details page (medicine_details.php)
# =============================================================================

import logging
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import MedicineDetailsPage as L, URLs

logger = logging.getLogger(__name__)


class MedicineDetailsPage(BasePage):

    def open(self) -> "MedicineDetailsPage":
        self.go_to(URLs.MEDICINE_DETAILS)
        self.wait.until(EC.presence_of_element_located(L.TABLE))
        return self

    def get_heading(self) -> str:
        return self.helpers.get_text(L.PAGE_HEADING)

    def is_on_page(self) -> bool:
        return "medicine_details.php" in self.get_current_url()

    # ── Add Medicine Details form ──────────────────────────────────────────────

    def select_medicine(self, medicine_name: str) -> "MedicineDetailsPage":
        """Select a medicine from the native <select> dropdown."""
        self.helpers.select_by_visible_text(L.MEDICINE_SELECT, medicine_name)
        return self

    def enter_packing(self, packing: str) -> "MedicineDetailsPage":
        self.helpers.type_text(L.PACKING_INPUT, packing)
        return self

    def click_save(self) -> None:
        self.helpers.click(L.SAVE_BTN)

    def add_medicine_detail(self, medicine_name: str, packing: str) -> None:
        """Fill and submit the Add Medicine Details form."""
        self.select_medicine(medicine_name)
        self.enter_packing(packing)
        self.click_save()
        logger.info(f"Medicine detail added: {medicine_name} / packing: {packing}")

    # ── DataTable ──────────────────────────────────────────────────────────────

    def search(self, keyword: str) -> None:
        self.helpers.search_datatable(L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return self.helpers.get_table_row_count(L.TABLE)

    def get_page_info_text(self) -> str:
        return self.helpers.get_text(L.PAGE_INFO)

    def get_cell_text(self, row: int, col: int) -> str:
        return self.helpers.get_table_cell_text("medicine_details", row, col)

    def click_edit_first_row(self) -> None:
        self.helpers.click(L.ANY_EDIT_BTN)
