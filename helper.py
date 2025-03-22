from faker import Faker

faker = Faker()


def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password


def generate_registration_data_too_small_password():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=5)
    return name, email, password


def verify_tab_state(driver, locator, expected_active):   # Функция для проверки состояния вкладок
    class_attribute = driver.find_element(*locator).get_attribute("class")
    if expected_active:
        assert "tab_tab_type_current__2BEPc" in class_attribute
    else:
        assert "tab_tab_type_current__2BEPc" not in class_attribute
