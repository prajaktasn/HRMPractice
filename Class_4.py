import unittest
from random import randrange, randint, random
from time import sleep

from selenium import webdriver


class Addition(unittest.TestCase):

    def setUp(self) ->None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://www.math.com/students/calculators/source/basic.htm")

        self.browser = browser

    def test_additon(self):
        window = self.browser
        num1 = randint(0, 9)
        num2 = randint(0, 10)
        #print(num1)
        #print(num2)
        #print(num1 + num2)
        window.find_element_by_name('Input').send_keys(num1)
        window.find_element_by_name('plus').click()
        sleep(10)
        window.find_element_by_name('Input').send_keys(num2)
        window.find_element_by_name('DoIt').click()
        sleep(10)

        actual_result = window.find_element_by_name('Input').get_attribute('value')
        sleep(10)

        self.assertEqual(str(num1 + num2), actual_result)


if __name__ == '__main__':
    unittest.main()
