import unittest
from time import sleep
from selenium import webdriver


class SearchQA(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def tearDown(self):
            self.browser.quit()

    def test_jobSearch(self):
        window = self.browser
        window.find_element_by_id('txtUsername').send_keys('admin')
        window.find_element_by_id('txtPassword').send_keys('password')
        window.find_element_by_id('btnLogin').click()

        sleep(5)

        window.find_element_by_id('empsearch_job_title').send_keys('QA Manager')
        window.find_element_by_id('empsearch_job_title').click()
        window.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[8]').click()
        window.find_element_by_id('searchBtn').click()
        sleep(5)

        first_row = '//*[@id="resultTable"]/tbody/tr'
        result_Jobtitle = window.find_element_by_xpath(first_row + '/td[5]').text

        self.assertEqual('QA Manager',result_Jobtitle)

















if __name__ == '__main__':
    unittest.main()
