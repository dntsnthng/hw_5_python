import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = os.getenv('window_width', '1600')
    browser.config.window_height = os.getenv('window_height', '1200')
    browser.config.timeout = float(os.getenv('timeout', '3.0'))
    browser.config.hold_browser_open = True