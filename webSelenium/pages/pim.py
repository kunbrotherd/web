from selenium.webdriver.common.by import By


class PimPage:
    pim_click = (By.XPATH, '//*[@href="/web/index.php/pim/viewPimModule"]')
    pim_configuration = (By.XPATH, '//*[@class="oxd-icon bi-chevron-down"')
    pim_employee_list = (By.LINK_TEXT, 'Employee List')
    pim_add_employee = (By.LINK_TEXT, 'Add Employee')
    pim_reports = (By.LINK_TEXT, 'Reports')
