from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Credentials
from locators import Locators
from curl import entrance


class TestTransferToPersonalAccount:

    def test_transfer_personal_account_click(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*Locators.LOG_OUT_BUTTON).click()
        assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.PAGE_INPUT))
        assert entrance == driver.current_url
