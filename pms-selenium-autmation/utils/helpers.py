# =============================================================================
# utils/helpers.py
# Reusable helper functions for waits, selects, alerts, and table utilities.
# =============================================================================

import time
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# ---------------------------------------------------------------------------
# Wait helpers
# ---------------------------------------------------------------------------

def wait_for_element(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = 10,
) -> WebElement:
    """Wait until an element is present in the DOM and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_clickable(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = 10,
) -> WebElement:
    """Wait until an element is visible and clickable, then return it."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_visible(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = 10,
) -> WebElement:
    """Wait until an element is visible on the page and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_url_contains(
    driver: WebDriver,
    fragment: str,
    timeout: int = 10,
) -> bool:
    """Wait until the current URL contains `fragment`."""
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(fragment)
    )


def wait_for_text_in_element(
    driver: WebDriver,
    locator: Tuple[str, str],
    text: str,
    timeout: int = 10,
) -> bool:
    """Wait until `text` appears inside the element at `locator`."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )


def is_element_present(
    driver: WebDriver,
    locator: Tuple[str, str],
) -> bool:
    """Return True if the element exists in the DOM (not necessarily visible)."""
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False


# ---------------------------------------------------------------------------
# Select / dropdown helpers
# ---------------------------------------------------------------------------

def select_by_visible_text(
    driver: WebDriver,
    locator: Tuple[str, str],
    text: str,
) -> None:
    """Select a <select> option by its visible text."""
    element = wait_for_element(driver, locator)
    Select(element).select_by_visible_text(text)


def select_by_value(
    driver: WebDriver,
    locator: Tuple[str, str],
    value: str,
) -> None:
    """Select a <select> option by its value attribute."""
    element = wait_for_element(driver, locator)
    Select(element).select_by_value(value)


# ---------------------------------------------------------------------------
# Select2 / AJAX dropdown helper
# ---------------------------------------------------------------------------

def select2_choose(
    driver: WebDriver,
    trigger_locator: Tuple[str, str],
    search_locator: Tuple[str, str],
    search_text: str,
    result_xpath_text: str,
    timeout: int = 10,
) -> None:
    """
    Interact with a Select2 widget.

    1. Click the Select2 trigger element to open the dropdown.
    2. Type `search_text` into the search box.
    3. Click the first result whose visible text matches `result_xpath_text`.

    Args:
        trigger_locator:   Locator for the Select2 container / span to click.
        search_locator:    Locator for the text input inside the opened dropdown.
        search_text:       Characters to type into the search box.
        result_xpath_text: Exact text of the option to click in the result list.
    """
    wait_for_clickable(driver, trigger_locator, timeout).click()
    search_box = wait_for_visible(driver, search_locator, timeout)
    search_box.send_keys(search_text)
    time.sleep(0.5)  # allow Ajax results to load
    option_xpath = (
        By.XPATH,
        f"//li[contains(@class,'select2-results__option') "
        f"and normalize-space(text())='{result_xpath_text}']",
    )
    wait_for_clickable(driver, option_xpath, timeout).click()


# ---------------------------------------------------------------------------
# DataTable / search helpers
# ---------------------------------------------------------------------------

def datatable_search(
    driver: WebDriver,
    search_locator: Tuple[str, str],
    keyword: str,
    pause: float = 0.5,
) -> None:
    """
    Type `keyword` into a DataTable search input and wait briefly
    for the client-side filter to apply.
    """
    search_box = wait_for_visible(driver, search_locator)
    search_box.clear()
    search_box.send_keys(keyword)
    time.sleep(pause)


def get_table_row_count(
    driver: WebDriver,
    table_locator: Tuple[str, str],
) -> int:
    """Return the number of <tr> elements in the table body."""
    table = wait_for_element(driver, table_locator)
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
    return len(rows)


# ---------------------------------------------------------------------------
# Alert helpers
# ---------------------------------------------------------------------------

def accept_alert(driver: WebDriver, timeout: int = 5) -> str:
    """Wait for a JS alert, capture its text, and accept it."""
    WebDriverWait(driver, timeout).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    text = alert.text
    alert.accept()
    return text


def dismiss_alert(driver: WebDriver, timeout: int = 5) -> str:
    """Wait for a JS alert, capture its text, and dismiss it."""
    WebDriverWait(driver, timeout).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    text = alert.text
    alert.dismiss()
    return text


# ---------------------------------------------------------------------------
# Miscellaneous
# ---------------------------------------------------------------------------

def scroll_to_element(driver: WebDriver, element: WebElement) -> None:
    """Scroll the page so that `element` is in the viewport."""
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)


def clear_and_type(
    driver: WebDriver,
    locator: Tuple[str, str],
    text: str,
) -> None:
    """Clear an input field and type `text` into it."""
    field = wait_for_clickable(driver, locator)
    field.clear()
    field.send_keys(text)


def get_element_text(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = 10,
) -> str:
    """Return the stripped visible text of an element."""
    return wait_for_visible(driver, locator, timeout).text.strip()