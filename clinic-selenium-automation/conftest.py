import pytest
from utils.driver_setup import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get("https://torejamedicalclinic.wuaze.com")
    yield driver
    driver.quit()