import allure
from data import UrlsList
from selenium.webdriver.support.ui import WebDriverWait
from locators.home_page_locators import LocatorsHomePage
from locators.switch_to_locators import LocatorsSwitchTo
from pages.base_page import BasePage

@allure.title('Тесты на проверку вопросов')
class HomePage(BasePage):

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        # Форматируем локаторы
        locator_q_formatted = self.format_locators(LocatorsHomePage.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(LocatorsHomePage.ANSWER_LOCATOR, num)
        self.scroll_to_element(LocatorsHomePage.QUESTION_LOCATOR_TO_SCROLL)
        self.wait_for_element(locator_q_formatted)
        self.click_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(LocatorsHomePage.LOGO_YANDEX)

    @allure.step("Клик по логотипу Скутера")
    def click_scooter_logo(self):
        self.click_element(LocatorsHomePage.LOGO_SCOOTER)

    @allure.step("Проверка отображения логотипа Дзен")
    def is_dzen_logo_displayed(self):
        return self.element_displayed(LocatorsSwitchTo.DZEN) and \
            self.get_current_url() == UrlsList.dzen

    @allure.step("Проверка отображения заголовка Самокат")
    def is_scooter_header_displayed(self):
        return self.element_displayed(LocatorsHomePage.HEADER) and \
            self.get_current_url() == UrlsList.home

    @allure.step("Переключение на окно по индексу")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открытие URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Закрыть баннер')
    def close_banner(self):
        self.click_element(LocatorsHomePage.POPUP_BUTTON)

    @allure.step("Прокрутка до кнопки заказа")
    def scroll_to_order_button(self, button_position):
        if button_position == "top":
            self.scroll_to_element(LocatorsHomePage.ORDER_BUTTON_1)
        elif button_position == "bottom":
            self.scroll_to_element(LocatorsHomePage.ORDER_BUTTON_2)

    @allure.step("Клик по кнопке заказа")
    def click_order_button(self, button_position):
        if button_position == "top":
            self.click_element(LocatorsHomePage.ORDER_BUTTON_1)
        elif button_position == "bottom":
            self.click_element(LocatorsHomePage.ORDER_BUTTON_2)


