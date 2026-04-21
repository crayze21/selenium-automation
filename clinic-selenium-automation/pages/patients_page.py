from selenium.webdriver.common.by import By
from .base_page import BasePage


class PatientsPage(BasePage):
    URL = "https://torejamedicalclinic.wuaze.com/patients.php"

    PATIENT_NAME_INPUT = (By.ID, "patient_name")
    ADDRESS_INPUT      = (By.ID, "address")
    CNIC_INPUT         = (By.ID, "cnic")
    DATE_OF_BIRTH_INPUT = (By.NAME, "date_of_birth")
    PHONE_NUMBER_INPUT = (By.ID, "phone_number")
    GENDER_INPUT = (By.ID, "gender")
    SAVE_PATIENT_BTN   = (By.ID, "save_Patient")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@role='dialog'])[1]")

    def add_patient(self, name, address, cnic, birth,phone, gender):
        self.type(*self.PATIENT_NAME_INPUT, name)
        self.type(*self.ADDRESS_INPUT, address)
        self.type(*self.CNIC_INPUT, cnic)
        self.type(*self.DATE_OF_BIRTH_INPUT, birth)
        self.type(*self.PHONE_NUMBER_INPUT, phone)
        self.type(*self.GENDER_INPUT, gender)
        self.click(*self.SAVE_PATIENT_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)