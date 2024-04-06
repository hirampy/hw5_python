import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.set_window_size(1080, 800)
    browser.config.type_by_js = False
    browser.config.timeout = 5.0

    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless=new')

    browser.config.driver_options = driver_options

    yield

    browser.quit()
