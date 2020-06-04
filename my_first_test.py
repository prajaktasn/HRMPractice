import unittest
from time import sleep

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self) ->None:
        browser  = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def test_valid_login(self):
        window = self.browser
        window.find_element_by_id('txtUsername').send_keys('admin')
        window.find_element_by_id('txtPassword').send_keys('password')
        window.find_element_by_id('btnLogin').click()
        welcome_message = window.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_message, "I can't")

    def test_invalid_login_no_username(self):
         window = self.browser
         window.find_element_by_id('txtUsername').send_keys('')
         window.find_element_by_id('txtPassword').send_keys('password')
         window.find_element_by_id('btnLogin').click()
         error_message = window.find_element_by_id('spanMessage').text
         self.assertEqual('Username cannot be empty', error_message, "I can't")

    def test_invalid_login_false_password(self):
         window = self.browser
         window.find_element_by_id('txtUsername').send_keys('admin')
         window.find_element_by_id('txtPassword').send_keys('pwd')
         window.find_element_by_id('btnLogin').click()
         error_message = window.find_element_by_id('spanMessage').text
         self.assertEqual('Invalid credentials', error_message, "I can't")



        # This is here for observation only

       # sleep(10)





if __name__ == '__main__':
    unittest.main()
