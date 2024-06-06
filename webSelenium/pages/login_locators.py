from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_text = (By.NAME, 'username')
    password_text = (By.NAME, 'password')
    login_sumit = (By.XPATH, ' //*[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')


