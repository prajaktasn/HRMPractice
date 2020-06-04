import unittest
from random import randint
from time import sleep

from faker import Faker
from selenium import webdriver

from fixtures.base_fixure import AdminTestCase


class AddEmployee(AdminTestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def tearDown(self):
        self.browser.quit()

    def test_add_employee(self):
        f = Faker()
        emp_id = (str)(randint(10000,1000000))
        first_name = f.first_name_male()
        last_name = f.last_name()
        username = f.user_name()
        password = f.password(6)

        print(emp_id)
        window = self.browser
        window.find_element_by_id('txtUsername').send_keys('admin')
        window.find_element_by_id('txtPassword').send_keys('password')
        window.find_element_by_id('btnLogin').click()

        window.find_element_by_id('btnAdd').click()
        sleep(5)
        window.find_element_by_id('firstName').send_keys(first_name)
        window.find_element_by_id('lastName').send_keys(last_name)
        window.find_element_by_id('employeeId').clear()
        window.find_element_by_id('employeeId').send_keys(emp_id)

        self.wait.until(Expected_Conditions)

        window.find_element_by_id('btnSave').click()
        sleep(5)

        page_header = window.find_element_by_css_selector('#pdMainContainer > div.head > h1').text
        self.assertEqual('Personal Details', page_header)
        window.find_element_by_id('menu_pim_viewPimModule').click()
        window.find_element_by_id('empsearch').send_keys(emp_id)
        window.find_element_by_id('searchBtn').click()
        sleep(10)

        first_row = '//*[@id="resultTable"]/tbody/tr'
        result_id = window.find_elements_by_xpath(first_row + '/td[2]/a').text
        result_first_name = window.find_elements_by_xpath(first_row + '/td[3]/a').text
        result_last_name = window.find_elements_by_xpath(first_row + '/td[4]/a').text

        self.assertEqual(emp_id, result_id)
        self.assertEqual(first_name, result_first_name)
        self.assertEqual(last_name, result_last_name)


if __name__ == '__main__':
    unittest.main()
