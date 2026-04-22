# =============================================================================
# utils/driver_factory.py
# Centralised WebDriver creation.
# Usage:  driver = DriverFactory.get_driver()
# =============================================================================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """
    Creates and configures a Selenium WebDriver instance.

    All driver options live here so that conftest.py and any
    standalone scripts only call DriverFactory.get_driver().
    """

    @staticmethod
    def get_driver(headless: bool = False) -> webdriver.Chrome:
        """
        Return a configured Chrome WebDriver.

        Args:
            headless: Run Chrome without a visible window.
                      Set to True in CI / headless environments.

        Returns:
            selenium.webdriver.Chrome instance (not yet pointed at a URL).
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if headless:
            options.add_argument("--headless=new")   # Chrome 112+ headless mode
            options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
        return driver