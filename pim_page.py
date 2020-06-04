from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from Test import BASE_URL


class PIMPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = BASE_URL + '/symfony/web/index.php/pim/viewEmployeeList'

    def do_add(self):
        self.browser.find_element_by_id('btnAdd').click()
        self.wait.until(EC.url_changes(self.page_url))

    def get_welcome_message(self):
        return self.browser.find_element_by_id('welcome').text

    def do_search_by_employee_id(self, emp_id):
        self.browser.find_element_by_id('empsearch_id').send_keys(emp_id)
        self.browser.find_element_by_id('searchBtn').click()
        self.wait.until(EC.text_to_be_present_in_element_value(
            (By.CSS_SELECTOR, '#empsearch_id'), emp_id))

    def get_id_from_row(self, row_number):
        return self.get_value_from_cell(row_number, 2)

    def get_name_from_row(self, row_number):
        return self.get_value_from_cell(row_number, 3)

    def get_last_name_from_row(self, row_number):
        return self.get_value_from_cell(row_number, 4)

    def get_value_from_cell(self, row_number, column_number):
        row = '//*[@id="resultTable"]/tbody/tr[{0}]'.format(row_number)
        return self.browser.find_element_by_xpath(row + '/td[{0}]'.format(column_number)).text