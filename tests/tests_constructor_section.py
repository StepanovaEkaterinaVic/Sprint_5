from locators import Locators


def verify_tab_state(driver, locator, expected_active):
    class_attribute = driver.find_element(*locator).get_attribute("class")
    if expected_active:
        assert "tab_tab_type_current__2BEPc" in class_attribute
    else:
        assert "tab_tab_type_current__2BEPc" not in class_attribute


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
