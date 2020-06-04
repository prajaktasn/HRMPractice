import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from Test import get_browser_session, BASE_URL, DEFAULT_WAIT
from Test.Common.utils import login


class SwitchToTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = get_browser_session()
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
        self.browser.get(BASE_URL)
        login(self.browser)

    def tearDown(self) -> None:
        self.browser

    def test_switching_to_new_window(self):
        browser = self.browser
        list_of_windows = browser.window_handles
        browser.find_element_by_class_name('subscribe').click()

        self.wait.until(EC.number_of_windows_to_be(1 + len(list_of_windows)))

        list_of_windows = browser.window_handles
        browser.switch_to.window(list_of_windows[-1])

        self.assertIn('User_Survey_Registration',browser.current_url)
        browser.switch_to.window(list_of_windows[0])
        self.assertIn(BASE_URL, browser.current_url)



if __name__ == '__main__':
    unittest.main()
