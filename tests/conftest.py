import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = os.getenv('window_width', '1600')
    browser.config.window_height = os.getenv('window_height', '1200')
    browser.config.hold_browser_open = True

    yield
    browser.quit()


