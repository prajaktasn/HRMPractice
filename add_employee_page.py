import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from Test import BASE_URL


class AddEmployeePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = BASE_URL + '/symfony/web/index.php/pim/addEmployee'

    def enter_employee_info(self, first_name, last_name, emp_id=None):
        self.wait.until(EC.presence_of_element_located(
            [By.ID, 'firstName'])).send_keys(first_name)
        self.browser.find_element_by_id('lastName').send_keys(last_name)

        if emp_id is not None:
            self.browser.find_element_by_id('employeeId').clear()
            self.browser.find_element_by_id('employeeId').send_keys(emp_id)

    def enter_employee_user_info(self, username, password):
        self.browser.find_element_by_id('chkLogin').click()

        self.wait.until(EC.visibility_of_element_located((By.ID, 'user_name'))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.ID, 'user_password'))).send_keys(password)
        self.browser.find_element_by_id('re_password').send_keys(password)

    def do_save(self):
        self.browser.find_element_by_id('btnSave').click()

    def wait_for_data_to_be_saved(self):
        self.wait.until_not(EC.url_contains('/admin/saveSystemUser'))