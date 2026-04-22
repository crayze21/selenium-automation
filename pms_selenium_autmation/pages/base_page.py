# =============================================================================
# pages/base_page.py
# All Page Object classes inherit from BasePage.
# BasePage wraps the most common Selenium actions so that page classes
# stay declarative and do not repeat boilerplate.
# =============================================================================

from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from utils.helpers import (
    wait_for_element,
    wait_for_clickable,
    wait_for_visible,
    wait_for_url_contains,
    clear_and_type,
    scroll_to_element,
    get_element_text,
    is_element_present,
)


class BasePage:
    """
    Base class for all Page Objects.

    Attributes:
        driver  – the active WebDriver session
        wait    – a WebDriverWait bound to the driver (default 10 s)
    """

    DEFAULT_TIMEOUT: int = 10

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def open(self, url: str) -> None:
        """Navigate the browser to `url`."""
        self.driver.get(url)

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def page_title(self) -> str:
        return self.driver.title

    def wait_for_url(self, fragment: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Block until the current URL contains `fragment`."""
        wait_for_url_contains(self.driver, fragment, timeout)

    # ------------------------------------------------------------------
    # Finding elements
    # ------------------------------------------------------------------

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Return element once it is present in the DOM."""
        return wait_for_element(self.driver, locator, self.DEFAULT_TIMEOUT)

    def find_visible(self, locator: Tuple[str, str]) -> WebElement:
        """Return element once it is visible."""
        return wait_for_visible(self.driver, locator, self.DEFAULT_TIMEOUT)

    def find_clickable(self, locator: Tuple[str, str]) -> WebElement:
        """Return element once it is clickable."""
        return wait_for_clickable(self.driver, locator, self.DEFAULT_TIMEOUT)

    def is_present(self, locator: Tuple[str, str]) -> bool:
        """Return True if element exists in the DOM."""
        return is_element_present(self.driver, locator)

    # ------------------------------------------------------------------
    # Interactions
    # ------------------------------------------------------------------

    def click(self, locator: Tuple[str, str]) -> None:
        """Click an element (waits until clickable first)."""
        self.find_clickable(locator).click()

    def type_text(self, locator: Tuple[str, str], text: str) -> None:
        """Clear the field and type `text` into it."""
        clear_and_type(self.driver, locator, text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Return the stripped visible text of an element."""
        return get_element_text(self.driver, locator, self.DEFAULT_TIMEOUT)

    def scroll_to(self, locator: Tuple[str, str]) -> None:
        """Scroll the element into the viewport."""
        element = self.find(locator)
        scroll_to_element(self.driver, element)

    # ------------------------------------------------------------------
    # Assertions helpers (return values so tests can assert freely)
    # ------------------------------------------------------------------

    def is_url_contains(self, fragment: str) -> bool:
        """Return True if the current URL contains `fragment`."""
        return fragment in self.driver.current_url

    def is_text_visible(self, locator: Tuple[str, str], text: str) -> bool:
        """Return True if `text` is found in the element's visible text."""
        try:
            element = wait_for_visible(self.driver, locator, 5)
            return text in element.text
        except TimeoutException:
            return False