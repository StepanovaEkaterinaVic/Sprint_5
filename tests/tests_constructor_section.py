from locators import Locators
from helper import verify_tab_state


class TestsNavigationSection:

    def test_navigate_to_sauces_section(self, driver):  # переход к разделу "Соусы"
        driver.find_element(*Locators.SAUCE_SECTION).click()
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_BREAD_SECTION, expected_active=False)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=True)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=False)

    def test_navigate_to_fillings_section(self, driver):  # переход к разделу "Начинки"
        driver.find_element(*Locators.FILLING_SECTION).click()
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_BREAD_SECTION, expected_active=False)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=False)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=True)

    def test_navigate_to_bread_section(self, driver):  # переход к разделу "Булки"
        driver.find_element(*Locators.FILLING_SECTION).click()
        driver.find_element(*Locators.BREAD_SECTION).click()
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_BREAD_SECTION, expected_active=True)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=False)
        verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=False)
