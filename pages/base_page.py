import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание элемента и проверка его отображения")
    def element_displayed(self, locator):
        element = self.find_element_with_wait(locator)
        return element.is_displayed()

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Заполнение локатора данными")
    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.find_element_with_wait(locator).text

    @allure.step('Отправка данных для заполнения поля')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Заполнение локатора данными')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        formatted_locator = locator.format(num)
        return (method, formatted_locator)

    @allure.step('Скролл до необходимого элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.location_once_scrolled_into_view
        return element

    @allure.step('Формирование динамического локатора')
    def get_dynamic_locator(self, locator_template, *args):
        return locator_template[0], locator_template[1].format(*args)
