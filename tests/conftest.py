import pytest
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser=request.config.getoption("browser_name")
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="D:\\driver\\October\\chromedriver.exe")
    #if browser == "firefox":
        #driver = webdriver.Firefox(executable_path="C:\\test3\\geckodriver.exe")
    # driver.implicitly_wait(40)


    driver.get("https://in.bookmyshow.com/explore/home/delhi")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()