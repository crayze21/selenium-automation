from pages.login_page import LoginPage
from pages.components.navbar import NavBar
from pages.patients_page import PatientsPage

def test_add_patient(driver):
    login = LoginPage(driver)
    login.open()
    login.login("admin", "admin123")

    nav = NavBar(driver)
    nav.go_to_patients()

    patients = PatientsPage(driver)
    patients.add_patient(
        "Juan Ponce",
        "Cubao",
        "123456789",
        "06/10/2000",
        "09674454611",
        "Male"
    )

    #wait and verify success
    message = patients.get_success_message()
    assert "Patient added successfully" in message.lower()
