import unittest
from time import sleep

from selenium import webdriver


class SearchEmployee(unittest.TestCase):

    def setUp(self) ->None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def test_search_by_name(self):
        browser = self.browser
        #login
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()
        sleep(3)

        #search by names
       # browser.find_element_by_id('empsearch_employee_name`_empName').click()
        #browser.find_element_by_id('empsearch_employee_name_empName').clear()
        browser.find_element_by_id('empsearch_employee_name_empName').send_keys('Bob')
        browser.find_element_by_id('searchBtn').click()
        sleep(2)

        search_result = browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]').text

        self.assertEqual('Bob', search_result)


if __name__ == '__main__':
    unittest.main()
