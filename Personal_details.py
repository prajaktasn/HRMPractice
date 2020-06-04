from pages.base_page import BasePage
from Test import BASE_URL


class PersonalDetailsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = BASE_URL + '/symfony/web/index.php/pim/viewEmployee/empNumber/3277'