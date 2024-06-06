from selenium.webdriver.common.by import By


class AdminPage:
    admin_link = (By.XPATH, '//*[@href="/web/index.php/admin/viewAdminModule"]')
    admin_add = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')

    admin_management = (By.XPATH, '//*[@class="oxd-icon bi-chevron-down"]')
    admin_job = (By.XPATH, '//span[contains(text(),"Job")]')
    admin_organization = (By.XPATH, '//span[contains(text(),"Organization")]')
    admin_qualification = (By.XPATH, '//span[contains(text(),"Qualifications")]')
    admin_nationalities = (By.LINK_TEXT, 'Nationalities')
    admin_corporate = (By.LINK_TEXT, 'Corporate Branding')
    admin_configuration = (By.XPATH, '//span[contains(text(),"Configuration")]')
