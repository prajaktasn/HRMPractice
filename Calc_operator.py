import unittest
from random import randint, random
from time import sleep

from selenium import webdriver


class Addition(unittest.TestCase):

    def setUp(self) ->None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://www.math.com/students/calculators/source/basic.htm")

        self.browser = browser

    def test_basic_addition(self):
        window = self.browser

        num1 = randint(0, 9)
        num2 = randint(0, 10)

        window.find_element_by_name('Input').send_keys(num1)
        window.find_element_by_name('plus').click()
        sleep(10)
        window.find_element_by_name('Input').send_keys(num2)
        window.find_element_by_name('DoIt').click()
        sleep(10)

        actual_result = window.find_element_by_name('Input').get_attribute('value')
        sleep(10)

        self.assertEqual(str(num1 + num2), actual_result)

    def test_random_operator(self):

        num1 = randint(0, 9)
        num2 = randint(0, 9)

        operator_selectors = ('times', 'div', 'plus', 'minus')
        operator = random.choice(operator_selectors)

        window = self.browser
        window.find_element_by_css_selector('input[value="  ' + str(num1) + '  "]').click()
        window.find_element_by_name(operator).click()
        window.find_element_by_xpath('//input[@value="  {0}  "]'.format(num2)).click()
        window.find_element_by_name('DoIt').click()

        actual_result = window.find_element_by_name('Input').get_attribute('value')

        if operator == 'plus':
            expected_result = num1 + num2
        elif operator == 'minus':
            expected_result = num1 - num2
        elif operator == 'times':
            expected_result = num1 * num2
        else:
            if num1 == 0 and num2 == 0:
                expected_result = 'NaN'
            elif num2 == 0:
                expected_result = 'Infinity'
            else:
                expected_result = num1 / num2

        self.assertEqual(str(expected_result), actual_result)

    def enter_number(self, number):
        for digit in list(str(number)):
            self.window.find_element_by_xpath('//input[@value="  {0}  "]'.format(digit)).click()

    def enter_random_number(self):
        number = randint(0, 99999)
        for digit in list(str(number)):
            self.window.find_element_by_xpath('//input[@value="  {0}  "]'.format(digit)).click()
        return number

    def test_calc_big_number(self):
        operator_selectors = ('times', 'div', 'plus', 'minus')
        operator = random.choice(operator_selectors)

        num1 = randint(0, 99999)
        window = self.browser

        self.enter_number(num1)

        window.find_element_by_name(operator).click()
        num2 = self.enter_random_number()

        window.find_element_by_name('DoIt').click()

        actual_result = window.find_element_by_name('Input').get_attribute('value')

        if operator == 'plus':
            expected_result = num1 + num2
        elif operator == 'minus':
            expected_result = num1 - num2
        elif operator == 'times':
            expected_result = num1 * num2
        else:
            if num1 == 0 and num2 == 0:
                expected_result = 'NaN'
            elif num2 == 0:
                expected_result = 'Infinity'
            else:
                expected_result = num1 / num2

        self.assertEqual(str(expected_result), actual_result)



if __name__ == '__main__':
    unittest.main()
