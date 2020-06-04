import unittest

from selenium.webdriver.support.wait import WebDriverWait

from Test import get_browser_session, BASE_URL, DEFAULT_WAIT
from Test.Common.utils import login, logout


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = get_browser_session()
        self.wait=WebDriverWait(self.browser,DEFAULT_WAIT)
        self.browser.get(BASE_URL)

    def tearDown(self) -> None:
        self.browser.quit()

class AdminTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        login(self.browser)

    def tearDown(self) -> None:
        logout(self.browser)
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
