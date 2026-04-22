# =============================================================================
# pages/base_page.py
# Base class for all Page Objects — shared navigation & common actions
# =============================================================================

import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import NavBar, URLs
from utils.helpers import Helpers
from utils.config import Config

logger = logging.getLogger(__name__)


class BasePage:
    """
    Every page object extends this class.
    Provides driver, wait, helpers, and shared navigation methods.
    """

    def __init__(self, driver: WebDriver):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.helpers = Helpers(driver)

    # ── Navigation ─────────────────────────────────────────────────────────────

    def go_to(self, url: str) -> None:
        """Navigate directly to a URL."""
        self.driver.get(url)
        logger.info(f"Navigated to: {url}")

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        return self.driver.title

    def refresh(self) -> None:
        self.driver.refresh()

    # ── Sidebar navigation methods ─────────────────────────────────────────────

    def click_dashboard(self) -> None:
        self.helpers.click(NavBar.MENU_DASHBOARD_LINK)

    def click_patients_menu(self) -> None:
        self.helpers.click(NavBar.MENU_PATIENTS_LINK)

    def go_to_new_prescription(self) -> None:
        self.click_patients_menu()
        self.helpers.click(NavBar.SUBMENU_NEW_RX)

    def go_to_add_patients(self) -> None:
        self.click_patients_menu()
        self.helpers.click(NavBar.SUBMENU_PATIENTS)

    def go_to_patient_history(self) -> None:
        self.click_patients_menu()
        self.helpers.click(NavBar.SUBMENU_HISTORY)

    def click_medicines_menu(self) -> None:
        self.helpers.click(NavBar.MENU_MEDICINES_LINK)

    def go_to_add_medicine(self) -> None:
        self.click_medicines_menu()
        self.helpers.click(NavBar.SUBMENU_ADD_MED)

    def go_to_medicine_details(self) -> None:
        self.click_medicines_menu()
        self.helpers.click(NavBar.SUBMENU_MED_DETAILS)

    def go_to_reports(self) -> None:
        self.helpers.click(NavBar.MENU_REPORTS_LINK)
        self.helpers.click(NavBar.SUBMENU_REPORTS)

    def go_to_users(self) -> None:
        self.helpers.click(NavBar.MENU_USERS_LINK)

    def logout(self) -> None:
        self.helpers.click(NavBar.LOGOUT_LINK)
        self.wait.until(EC.url_contains("index.php"))
        logger.info("Logged out successfully")

    # ── Shared assertions ──────────────────────────────────────────────────────

    def is_logged_in(self) -> bool:
        """Check if the user is currently authenticated."""
        try:
            text = self.driver.find_element(*NavBar.WELCOME_TEXT).text
            return "Welcome" in text
        except Exception:
            return False

    def get_welcome_text(self) -> str:
        return self.helpers.get_text(NavBar.WELCOME_TEXT)
