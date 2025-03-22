from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import helper as hp


class TestRegistrationWithNewInputData:

    def test_success_registration(self, driver):
        name, email, password = hp.generate_registration_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_POPUP).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PAGE_INPUT))


class TestCheckingCreationExistingAccount:

    def test_failed_registration_too_small_password(self, driver):
        name, email, password = hp.generate_registration_data_too_small_password()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_POPUP).click()
        error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert "Некорректный пароль" in error_message
