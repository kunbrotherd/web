
from selenium.webdriver.support.wait import WebDriverWait

from webSelenium.pages.admin import AdminPage
from webSelenium.pages.base_public_method import BasePage
from webSelenium.pages.login_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    # 输入用户名
    def enter_username(self, username):
        # 智能等待加载这个元素，等待加载用户名这个文本框
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.username_text))
        # 用户名元素定位，加“*”是将元组格式拆成两个参数
        element = self.driver.find_element(*LoginPageLocators.username_text)
        # 单击
        element.click()
        # 清除文本框
        element.clear()
        # 输入内容
        element.send_keys(username)

    # 输入密码
    def enter_password(self, password):
        # 智能等待加载这个元素，等待加载密码这个文本框
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.password_text))
        # 元素定位
        element = self.driver.find_element(*LoginPageLocators.password_text)
        # 单击
        element.click()
        # 清除文本框
        element.clear()
        # 输入内容
        element.send_keys(password)

    # 单击登录
    def click_login(self):

        element_c = self.driver.find_element(*LoginPageLocators.login_sumit)
        element_c.click()

    # 返回验证的文本
    def result_login(self):
        # 验证welcome admin(text)出现,presence_of_element_located(locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(AdminPage.admin_link))
        return self.driver.find_element(*AdminPage.admin_link).text
