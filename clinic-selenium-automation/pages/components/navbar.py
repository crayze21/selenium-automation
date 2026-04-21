from selenium.webdriver.common.by import By
from ..base_page import BasePage


class NavBar(BasePage):
    MENU_PATIENTS_LINK = (By.CSS_SELECTOR, "#mnu_patients > a")
    SUBMENU_PATIENTS   = (By.ID, "mi_patients")

    def go_to_patients(self):
        self.click(*self.MENU_PATIENTS_LINK)
        self.click(*self.SUBMENU_PATIENTS)