from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Test import ADMIN_PASSWORD, SHORT_WAIT


def login(browser, username='admin', password=ADMIN_PASSWORD):
    browser.find_element_by_id('txtUsername').send_keys(username)
    browser.find_element_by_id('txtPassword').send_keys(password)
    browser.find_element_by_id('btnLogin').click()

    wait = WebDriverWait(browser, SHORT_WAIT)
    # if username == 'admin':
    if browser.find_elements_by_id('employee-information'):
        wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint')))
def logout(browser):
    browser.find_element_by_link_text('Logout').click()