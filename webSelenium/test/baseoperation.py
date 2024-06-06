import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webSelenium.utils.get_path import get_par_path

# 设置chromedriver的路径
executable_path = r'C:\Users\86137\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建一个Service对象，传入chromedriver的路径
service = Service(executable_path)
# 创建一个webriver对象，传入service对象
driver = webdriver.Chrome(service=service)
# driver.get(url='http://www.baidu.com')
# driver.find_element(by=By.ID, value='kw').send_keys('麻婆杜甫')
# time.sleep(2)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

time.sleep(3)
# 登录输入用户名密码密码
driver.find_element(By.NAME, 'username').send_keys('admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
# 点击登录按钮
driver.find_element(By.XPATH, ' //*[@class="oxd-button oxd-button--medium '
                              'oxd-button--main orangehrm-login-button"]').click()

pic_path = os.path.join(get_par_path(), 'shootpicture\\')
time_now = str(datetime.now()).replace(':', '_')

print(time_now)
time.sleep(3)
driver.save_screenshot(pic_path + time_now + 'admin1.png')

# # 进入admin链接界面
# driver.find_element(By.XPATH, ' //*[@href="/web/index.php/admin/viewAdminModule"]').click()
# time.sleep(1)
# # add添加按钮
# # driver.find_element(By.XPATH, ' //*[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
#
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@class="oxd-icon bi-chevron-down"]').click()
# # user Role
# # driver.find_element(By.XPATH, ' //*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]').click()
#
# time.sleep(3)
# driver.find_element(By.XPATH, '//span[contains(text(),"Organization")]').click()
#
#
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, 'General Information').click()
# 进入PIM链接界面
# driver.find_element(By.XPATH, ' //*[@href="/web/index.php/pim/viewPimModule"]').click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, 'Reports').click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, 'Add Employee').click()
# time.sleep(4)
#
# driver.find_element(By.XPATH, '//*[@class="oxd-icon bi-chevron-down"]').click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, 'Custom Fields').click()
# time.sleep(4)
#
# driver.find_element(By.XPATH, '//*[@class="oxd-icon bi-chevron-down"]').click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, 'Termination Reasons').click()
time.sleep(3)
driver.close()
