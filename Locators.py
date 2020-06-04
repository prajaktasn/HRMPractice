import unittest
from time import sleep

from selenium import webdriver


class Logo(unittest.TestCase):

    def setUp(self) ->None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def tearDown(self):
            self.browser.quit()

    def test_logo(self):
        window = self.browser
        window.find_element_by_id('txtUsername').send_keys('admin')
        window.find_element_by_id('txtPassword').send_keys('password')
        window.find_element_by_id('btnLogin').click()

        window.find_element_by_css_selector('#branding > img')
        window.find_element_by_xpath('//*[@id="branding"]/img')

        window.find_element_by_css_selector('[width="283"][height="56"]')
        window.find_element_by_xpath('//img[@width="283" and @height="56"]')

        window.find_element_by_css_selector('[alt="OrangeHRM"]')
        window.find_element_by_xpath('//img[@alt="OrangeHRM"]')

        window.find_element_by_css_selector('#wrapper img')
        window.find_element_by_xpath('//*[@id="wrapper"]//img')

        window.find_element_by_css_selector('img')
        window.find_element_by_xpath('//img')

        logo = window.find_element_by_xpath('//img')

        logo_location = logo.location
        logo_size = logo.size

        document_size = window.find_element_by_tag_name('body').size

        x = logo_location['x'] + logo_size['width']
        y = logo_location['y'] + logo_size['height']

        bottom_right_corner = {'x': x, 'y': y}

        self.assertTrue(document_size['width'] / 3 > bottom_right_corner['x'])
        self.assertTrue(document_size['height'] / 4 > bottom_right_corner['y'])


if __name__ == '__main__':
    unittest.main()
