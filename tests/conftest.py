import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()