# =============================================================================
# pages/medicines_page.py
# =============================================================================

from pages.base_page import BasePage
from locators.locators import MedicinesPage as L, URLs
from utils.helpers import datatable_search, get_table_row_count


class MedicinesPage(BasePage):
    """Page Object for medicines.php."""

    def open_medicines_page(self) -> None:
        self.open(URLs.MEDICINES)

    # ------------------------------------------------------------------
    # Add Medicine form
    # ------------------------------------------------------------------

    def enter_medicine_name(self, name: str) -> None:
        self.type_text(L.MEDICINE_NAME_INPUT, name)

    def click_save_medicine(self) -> None:
        self.click(L.SAVE_MEDICINE_BTN)

    def add_medicine(self, name: str) -> None:
        self.enter_medicine_name(name)
        self.click_save_medicine()

    # ------------------------------------------------------------------
    # Table / search
    # ------------------------------------------------------------------

    def search_medicine(self, keyword: str) -> None:
        datatable_search(self.driver, L.SEARCH_INPUT, keyword)

    def get_row_count(self) -> int:
        return get_table_row_count(self.driver, L.TABLE)

    def get_page_info_text(self) -> str:
        return self.get_text(L.PAGE_INFO)

    def get_column_headers(self) -> list[str]:
        return [
            self.get_text(L.TH_SNO),
            self.get_text(L.TH_MEDICINE_NAME),
            self.get_text(L.TH_ACTION),
        ]

    def click_medicine_name_header(self) -> None:
        self.click(L.TH_MEDICINE_NAME)

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def click_csv_export(self) -> None:
        self.click(L.CSV_BTN)