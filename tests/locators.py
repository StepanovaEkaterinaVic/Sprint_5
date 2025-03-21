from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    REG_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # Поле ввода имени
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  # Поле ввода email
    PASSWORD = (By.XPATH, "//input[@type='password' and @name='Пароль']")  # Поле ввода пароля
    REG_POPUP = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # Сообщение об ошибке
    REG_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти"
    PAGE_INPUT = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Надпись "Вход" на странице входа
    INPUT_BUTTON = (By.XPATH, "//button[text()='Войти']")   # Надпись "Войти" на странице авторизации
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # кнопка Восстановить пароль на странице авторизации
    CHANGE_DATA_PAGE = (By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")
    CONSTRUKTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") ## Кнопка конструктор на странице личный кабинет
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ" (для зарегистрированных)
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")  # Логотип сайта
    LOG_OUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка выход на страниче личный кабинет
    BREAD_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")  # Раздел "Булки"
    SAUCE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
    FILLING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
    SAUCE_ACTIVE_BREAD_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Булки')]]")  # Раздел "Булки" не активен
    SAUCE_ACTIVE_SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Соусы')]]")  # Раздел "Соусы" активен
    SAUCE_ACTIVE_FILLING_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Начинки')]]")  # Раздел "Начинки" не активен