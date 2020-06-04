import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SearchQA(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def tearDown(self):
        self.browser.quit()

    def test_jobSearch(self):
        expected_job_title = 'QA Manager'
        window = self.browser
        window.find_element_by_id('txtUsername').send_keys('admin')
        window.find_element_by_id('txtPassword').send_keys('password')
        window.find_element_by_id('btnLogin').click()

        sleep(5)

        Select(window.find_element_by_id('empsearch_job_title')).select_by_visible_text(expected_job_title)

        window.find_element_by_id('searchBtn').click()

        sleep(2)

        all_rows = window.find_element_by_css_selector('#resultTable tr')

        for single_row in all_rows:
            result_job_title = single_row.find_element_by_css_selector('td:nth-child(5)').text
            self.assertEqual(expected_job_title, result_job_title)

    def test_search_by_name(self):
       expected_name = 'Bob'

       window = self.browser
       window.find_element_by_id('txtUsername').send_keys('admin')
       window.find_element_by_id('txtPassword').send_keys('password')
       window.find_element_by_id('btnLogin').click()

       sleep(5)

       window.find_element_by_id('empsearch_employee_name_empName').send_keys(expected_name + Keys.ESCAPE)
       window.find_element_by_id('searchBtn').click()

       sleep(5)

       all_rows = window.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr')

       for single_row in all_rows:
           # first_row = '//*[@id="resultTable"]/tbody/tr'
           # result_job_title = window.find_element_by_xpath(first_row + '/td[3]/a').text

         result_job_title = single_row.find_element_by_xpath('.//td[3]/a').text

         self.assertEqual(expected_name, result_job_title)




















