from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Credentials
from locators import Locators
from tests.curl import main_site


class TestTransferFromPersonalAccount:

    def test_transfer_from_personal_account_to_constructor(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.CHANGE_DATA_PAGE))
        driver.find_element(*Locators.CONSTRUKTOR_BUTTON).click()
        assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert main_site == driver.current_url

    def test_transfer_from_personal_account_to_logo_click(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.CHANGE_DATA_PAGE))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert main_site == driver.current_url
