import unittest
from time import sleep

from selenium import webdriver

from fixtures.base_fixure import BaseTestCase


class SocialMediaTest(BaseTestCase):

    def setUp(self) ->None:
        browser = webdriver.Chrome(executable_path='C:\\PersonalData\\portnov\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe')
        browser.get("http://hrm-online.portnov.com/")

        self.browser = browser

    def test_social_media(self):
        self.browser.quit()

    def test_valid_login(self):
        window = self.browser
        self.assertRegex(window.page_source, 'value="([a-f0-9]+)" .+=csrf_token')
        social_icon_link = window.find_element_by_css_selector('#social-icons a')
        link_url = social_icon_link.get_attribute('href')
        domain = link_url.split('.')[1]
        icon_img = social_icon_link.find_element_by_tag_name('img')
        img_src = icon_img.get_attribute('src')
        self.assertTrue(img_src.find(domain) >= 0)

        self.assertIn(domain, img_src)
        alt_text = icon_img.get_attribute('alt')
        self.assertIn(domain.lower(), alt_text.lower())

        domain = 'youtube'

        icon_img = window.find_element_by_xpath('//img[contains(@alt, "{0}")]'.format(domain))
        self.assertIn(domain, icon_img.get_attribute('src'))

        parent_link_element = icon_img.find_element_by_xpath('.//..')
        self.assertIn(domain, parent_link_element.get_attribute('href'))




if __name__ == '__main__':
    unittest.main()
