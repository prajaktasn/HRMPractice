import os

from selenium import webdriver

BROWSER = 'chrome'

DEFAULT_WAIT = 10
SHORT_WAIT = 5

BASE_URL = 'http://hrm-online.portnov.com'
ADMIN_PASSWORD = 'password'

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

_file_ext = ''
if os.name == 'nt':
    _file_ext = '.exe'

_firefox_browser_executable = TEST_DIR + "/../browserdrivers/geckodriver" + _file_ext

def get_browser_session(browser_type=BROWSER):
    if browser_type.lower() == 'chrome' or browser_type.lower() == 'googlechrome':
        browser = webdriver.Chrome(executable_path=TEST_DIR + "/../browserdrivers/chromedriver_win32/chromedriver" + _file_ext)
    elif browser_type.lower() == 'firefox':
        browser = webdriver.Firefox(executable_path=_firefox_browser_executable)

    else:
        raise TypeError(
            'The browser type "{0}" that you specified is currently not supported. Please try another option.'.format(
                browser_type))
    return browser






_file_ext = ''
if os.name == 'nt':
    _file_ext = '.exe'

CHROME_EXE_PATH = TEST_DIR + '/../browserdrivers/chromedriver_win32' + _file_ext
FIREFOX_EXE_PATH = TEST_DIR + '/../browsers/geckodriver' + _file_ext
