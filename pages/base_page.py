import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def is_element_present(self, locator, time=50):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def await_for_invisible_element(self, locator, time=50):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element(locator))

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def return_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Перейти по адресу')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Перетянуть элемент')
    def drag_and_drop_ingredient(self, locator_from, locator_to):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

