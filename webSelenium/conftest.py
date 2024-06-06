import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.feature('打开浏览器')
@pytest.fixture(scope='session', autouse=True)
def init_driver(request):
    driver_path = r'C:\Users\86137\AppData\Local\Google\Chrome\Application\chromedriver.exe'
    # 创建一个Service对象，传入chromedriver的路径
    service = Service(driver_path)
    # 创建一个webriver对象，传入service对象
    driver = webdriver.Chrome(service=service)

    def close_browser():
        driver.quit()
        request.addfinalizer(close_browser())
    return driver
