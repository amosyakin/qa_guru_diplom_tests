import os

import pytest
from dotenv import load_dotenv

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from flex_kino_project_tests.utils import attach


load_dotenv()

user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = 'https://flex-kino.com'
    browser.config.window_width = 1366
    browser.config.window_height = 768

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
