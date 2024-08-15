from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    CREATE_BURGER_TEXT = (By.XPATH, '//h1[text()="Соберите бургер"]')
    BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    OPENED_MODAL_BOX = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    CLOSE_MODAL_BOX = (By.XPATH, '//button[contains(@class,"close")]')
    PRICE_NUMBER = (By.XPATH, '//p[contains (@class, "text text_type_digits-medium")]')
    LOWER_HALF_FOR_INGREDIENT = (By.XPATH, '//div[contains (@class, "constructor-element_pos_bottom")]')
    INGREDIENT_COUNTER = (By.XPATH, '//p[contains(@class, "counter_counter")]')
    ORDER_MODAL_BOX = (By.XPATH, '//p[text()="идентификатор заказа"]')
    CLOSE_ORDER_BOX = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')
    TRASH_ELEMENT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                                "/following::div[@class='Modal_modal_overlay__x2ZCr']")
    DEFAULT_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

class FeedPageLocators:
    FEED_TEXT = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]')
    ORDER_MODAL_BOX = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                 '/child::div[contains(@class, "Modal_modal__container")]')
    NUMBER_OF_ORDERS = (By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]//p[@class="text '
                                'text_type_digits-default"]')
    COUNTER_FOR_ALL_TIME = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']
    COUNTER_FOR_TODAY = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']
    IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
    ALL_READY_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')

class PersonalAccountLocators:
    HISTORY_OF_ORDERS = (By.XPATH, '//a[text()="История заказов"]')
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    RECOVER_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')

class RecoverPasswordLocators:
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')

class ResetPasswordLocators:
    NEW_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    ACTIVE_NEW_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')
