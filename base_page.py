from selenium.webdriver.support.wait import WebDriverWait

from Test import DEFAULT_WAIT


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)
        self.page_url = None

    def get_header(self):
        return self.browser.find_element_by_css_selector('div.head > h1').text

    def go_to_page(self):
        self.browser.get(self.page_url)