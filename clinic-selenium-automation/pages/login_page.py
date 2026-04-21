from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://torejamedicalclinic.wuaze.com/index.php"

    USERNAME_INPUT = (By.ID, "user_name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.NAME, "login")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(*self.USERNAME_INPUT, username)
        self.type(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)