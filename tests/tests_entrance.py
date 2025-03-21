from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Credentials
from locators import Locators
from tests.curl import main_site


class TestLoginButton:

    def test_login_button_on_homepage(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.url_changes(main_site))

    def test_login_button_on_personal_cabinet(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.url_changes(main_site))

    def test_login_button_on_form_registration(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.url_changes(main_site))

    def test_login_button_on_password_recovery_form(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.RECOVERY_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.url_changes(main_site))

