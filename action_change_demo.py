import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Test import get_browser_session, BASE_URL, SHORT_WAIT
from Test.Common.utils import login
from fixtures.base_fixure import BaseTestCase


class ActionTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        login(self.browser)

    def test_navigate_to_work_week_page(self):
        browser = self.browser
        current_url = browser.current_url

        actions = ActionChains(browser)
        actions.move_to_element(browser.find_element_by_id('menu_leave_viewLeaveModule'))
        actions.move_to_element(browser.find_element_by_id('menu_leave_Entitlements'))
        actions.move_to_element(browser.find_element_by_id('menu_leave_Configure'))
        actions.click(browser.find_element_by_id('menu_leave_defineWorkWeek'))
        actions.perform()

        WebDriverWait(browser, SHORT_WAIT).until(EC.url_changes(current_url))

        WebDriverWait(browser, SHORT_WAIT).until(EC.url_to_be(BASE_URL + '/symfony/web/index.php/leave/defineWorkWeek'))

        self.assertEqual('Work Week', browser.find_element_by_css_selector('.head>h1').text)



if __name__ == '__main__':
    unittest.main()
