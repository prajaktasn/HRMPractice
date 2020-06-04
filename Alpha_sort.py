import unittest
from time import sleep

from selenium import webdriver

from Test.Common.utils import login


class MyTestCase(unittest.TestCase):

    def setUp(self) ->None:
        browser  = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def test_valid_login(self):
        window = self.browser
       # window.find_element_by_id('txtUsername').send_keys('admin')
        #window.find_element_by_id('txtPassword').send_keys('password')
        #window.find_element_by_id('btnLogin').click()

        login(window)

        sleep(3)

        window.find_element_by_link_text('First (& Middle) Name').click()
        sleep(2)

        previous = ' '

        all_first_name_links = window.find_elements_by_xpath('//td[3]/a')

        for first_name in all_first_name_links:
            next_text = first_name.text

            self.assertLessEqual(previous, next_text)
            previous = next_text



if __name__ == '__main__':
    unittest.main()
