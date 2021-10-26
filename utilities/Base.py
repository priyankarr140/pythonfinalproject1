import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class BaseClass:
    def callActiveElement(self,driver):
        driver.switch_to.active_element

    def takescreenshot(self,driver):
        driver.save_screenshot(".//screenshot//bill.png")

    def explicitwait(self,driver,value):
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,value)))
        driver.find_element_by_class_name(value).click()

    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs

