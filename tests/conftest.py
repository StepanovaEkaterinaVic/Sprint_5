import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from curl import *


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()



