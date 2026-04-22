# =============================================================================
# utils/driver_factory.py
# Creates and configures the Selenium WebDriver instance
# =============================================================================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config import Config


class DriverFactory:

    @staticmethod
    def get_driver() -> webdriver.Remote:
        """Return a configured WebDriver based on Config settings."""
        browser = Config.BROWSER.lower()

        if browser == "chrome":
            return DriverFactory._chrome_driver()
        elif browser == "firefox":
            return DriverFactory._firefox_driver()
        else:
            raise ValueError(f"Unsupported browser: '{browser}'. Use 'chrome' or 'firefox'.")

    # ── Chrome ─────────────────────────────────────────────────────────────────
    @staticmethod
    def _chrome_driver() -> webdriver.Chrome:
        options = webdriver.ChromeOptions()

        if Config.HEADLESS:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        DriverFactory._configure(driver)
        return driver

    # ── Firefox ────────────────────────────────────────────────────────────────
    @staticmethod
    def _firefox_driver() -> webdriver.Firefox:
        options = webdriver.FirefoxOptions()

        if Config.HEADLESS:
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        DriverFactory._configure(driver)
        return driver

    # ── Shared config ──────────────────────────────────────────────────────────
    @staticmethod
    def _configure(driver) -> None:
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
