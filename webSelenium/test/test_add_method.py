from datetime import datetime
import os
import time

import allure
import pytest

from webSelenium.pages.base_public_method import BasePage
from webSelenium.pages.login_method import LoginPage
from webSelenium.utils.get_path import get_par_path, get_yaml_data


class TestClass:

    @allure.step('从配置文件中读取登录数据')
    @pytest.fixture()
    def login_data(self):
        yaml_path = os.path.join(get_par_path(), 'config/config.yaml')
        test_data = get_yaml_data(yaml_path)
        return test_data

    @allure.feature('登录功能')
    @allure.step('使用管理员身份登录')
    def test_login(self, init_driver, login_data):

        init_driver.get(login_data['url'])
        init_driver.minimize_window()
        init_driver.implicitly_wait(30)
        base_page = BasePage(init_driver)
        with allure.step('初始化网页'):
            login_page = LoginPage(init_driver)
        with allure.step('输入用户名和密码后单击登录'):
            login_page.enter_username(login_data['username'])
            login_page.enter_password(login_data['password'])
            login_page.click_login()
        with allure.step('断言admin是否登录成功并截图'):
            # assert 'admin' in login_page.result_login()
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            time.sleep(2)
            base_page.save_picture(pic_path + str(datetime.now()).replace(':', '_') + 'login.png')


