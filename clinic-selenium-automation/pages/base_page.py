from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, by, value):
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def type(self, by, value, text):
        self.wait.until(EC.visibility_of_element_located((by, value))).send_keys(text)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait_visible(locator).text