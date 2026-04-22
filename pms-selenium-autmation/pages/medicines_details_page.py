# =============================================================================
# pages/medicine_details_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import MedicineDetailsPage as L, URLs
from utils.helpers import datatable_search, get_table_row_count, select_by_visible_text


class MedicineDetailsPage(BasePage):
    """Page Object for medicine_details.php."""

    def open_medicine_details_page(self) -> None:
        self.open(URLs.MEDICINE_DETAILS)

    # ------------------------------------------------------------------
    # Add Medicine Detail form
    # ------------------------------------------------------------------

    def select_medicine(self, medicine_name: str) -> None:
        select_by_visible_text(self.driver, L.MEDICINE_SELECT, medicine_name)

    def enter_packing(self, packing: str) -> None:
        self.type_text(L.PACKING_INPUT, packing)

    def click_save(self) -> None:
        self.click(L.SAVE_BTN)

    def add_medicine_detail(self, medicine_name: str, packing: str) -> None:
        self.select_medicine(medicine_name)
        self.enter_packing(packing)
        self.click_save()

    # ------------------------------------------------------------------
    # Table / search
    # ------------------------------------------------------------------

    def search_medicine_detail(self, keyword: str) -> None:
        datatable_search(self.driver, L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return get_table_row_count(self.driver, L.TABLE)

    def get_column_headers(self) -> list[str]:
        return [
            self.get_text(L.TH_SNO),
            self.get_text(L.TH_MEDICINE_NAME),
            self.get_text(L.TH_PACKING),
            self.get_text(L.TH_ACTION),
        ]