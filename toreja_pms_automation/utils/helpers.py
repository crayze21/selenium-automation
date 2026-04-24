# =============================================================================
# utils/helpers.py
# Reusable helper functions for Selenium interactions
# =============================================================================

import os
import time
import logging
from datetime import datetime

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from utils.config import Config

logger = logging.getLogger(__name__)


class Helpers:
    pass
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    # ── Waits ──────────────────────────────────────────────────────────────────

    def wait_for_element(self, locator: tuple) -> WebElement:
        """Wait until an element is present and visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple) -> WebElement:
        """Wait until an element is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, partial_url: str, timeout: int = None) -> bool:
        """Wait until the current URL contains a given string."""
        t = timeout or Config.EXPLICIT_WAIT
        return WebDriverWait(self.driver, t).until(EC.url_contains(partial_url))

    def wait_for_text_in_element(self, locator: tuple, text: str) -> bool:
        """Wait until an element's text contains the given string."""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_element_invisible(self, locator: tuple) -> bool:
        """Wait until an element is not visible."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # ── Actions ────────────────────────────────────────────────────────────────

    def click(self, locator: tuple) -> None:
        """Wait for element to be clickable, then click it."""
        element = self.wait_for_clickable(locator)
        element.click()
        logger.debug(f"Clicked: {locator}")

    def type_text(self, locator: tuple, text: str, clear: bool = True) -> None:
        """Wait for element, optionally clear it, then type text."""
        element = self.wait_for_element(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        logger.debug(f"Typed '{text}' into: {locator}")

    def get_text(self, locator: tuple) -> str:
        """Return the visible text of an element."""
        return self.wait_for_element(locator).text.strip()

    def get_value(self, locator: tuple) -> str:
        """Return the value attribute of an input element."""
        return self.wait_for_element(locator).get_attribute("value")

    def is_displayed(self, locator: tuple) -> bool:
        """Return True if element is visible, False otherwise."""
        try:
            return self.driver.find_element(*locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def is_enabled(self, locator: tuple) -> bool:
        """Return True if element is enabled."""
        try:
            return self.driver.find_element(*locator).is_enabled()
        except NoSuchElementException:
            return False

    # ── Select / Dropdowns ─────────────────────────────────────────────────────

    def select_by_visible_text(self, locator: tuple, text: str) -> None:
        """Select a native <select> option by visible text."""
        element = self.wait_for_element(locator)
        Select(element).select_by_visible_text(text)
        logger.debug(f"Selected '{text}' in: {locator}")

    def select_by_value(self, locator: tuple, value: str) -> None:
        """Select a native <select> option by value attribute."""
        element = self.wait_for_element(locator)
        Select(element).select_by_value(value)

    def get_selected_option(self, locator: tuple) -> str:
        """Return the currently selected option text from a <select>."""
        element = self.wait_for_element(locator)
        return Select(element).first_selected_option.text.strip()

    # ── Select2 Dropdowns (custom jQuery plugin) ───────────────────────────────

    def select2_choose(self, trigger_locator: tuple, search_input_locator: tuple, option_text: str) -> None:
        """
        Interact with a Select2 dropdown:
        1. Click the visible Select2 trigger.
        2. Type in the search box.
        3. Click the matching dropdown option.
        """
        self.click(trigger_locator)
        time.sleep(0.3)
        self.type_text(search_input_locator, option_text, clear=False)
        time.sleep(0.5)
        # Find and click the first matching result in the Select2 dropdown
        option_locator = (
            "xpath",
            f"//li[contains(@class,'select2-results__option') and contains(text(),'{option_text}')]"
        )
        self.click(option_locator)

    def set_date_via_js(self, locator: tuple, date_value: str) -> None:
        """
        Set a date input value via JavaScript (bypasses custom date pickers).
        date_value format: 'YYYY-MM-DD'
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            element, date_value
        )
        logger.debug(f"Set date '{date_value}' on: {locator}")

    # ── DataTable helpers ──────────────────────────────────────────────────────

    def get_table_row_count(self, table_locator: tuple) -> int:
        """Return number of visible rows in a DataTable tbody."""
        from selenium.webdriver.common.by import By
        table = self.wait_for_element(table_locator)
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        return len([r for r in rows if r.text.strip()])

    def get_table_cell_text(self, table_id: str, row: int, col: int) -> str:
        """Return the text of a DataTable cell (1-indexed row and column)."""
        from selenium.webdriver.common.by import By
        selector = f"#{table_id} tbody tr:nth-child({row}) td:nth-child({col})"
        return self.driver.find_element(By.CSS_SELECTOR, selector).text.strip()

    def search_datatable(self, search_locator: tuple, keyword: str) -> None:
        """Type a keyword into a DataTable search input."""
        self.type_text(search_locator, keyword)
        time.sleep(0.8)   # allow DataTable to re-render

    # ── Screenshot ─────────────────────────────────────────────────────────────

    def take_screenshot(self, name: str = "screenshot") -> str:
        """Save a screenshot and return its file path."""
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(Config.SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(path)
        logger.info(f"Screenshot saved: {path}")
        return path

    # ── JavaScript utilities ───────────────────────────────────────────────────

    def scroll_to_element(self, locator: tuple) -> None:
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, locator: tuple) -> None:
        """Click an element using JavaScript (useful when normal click is intercepted)."""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
