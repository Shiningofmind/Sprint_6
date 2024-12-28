import allure
from locators.order_page_locators import LocatorsOrderPage
from pages.base_page import BasePage



class OrderPage(BasePage):
    @allure.step('Заполнение заказа')
    def fill_order_form(self, first_name, last_name, address, phone, comment, metro, rent, color, data):
        self.add_text_to_element(LocatorsOrderPage.NAME_INPUT_FIELD, first_name)
        self.add_text_to_element(LocatorsOrderPage.SURNAME_INPUT_FIELD, last_name)
        self.add_text_to_element(LocatorsOrderPage.ADDRESS_INPUT_FIELD, address)
        self.click_element(LocatorsOrderPage.METRO)
        metro_locator = self.get_dynamic_locator(LocatorsOrderPage.METRO_STATION_TEMPLATE, metro)
        self.click_element(metro_locator)
        self.add_text_to_element(LocatorsOrderPage.PHONE_INPUT_FIELD, phone)
        self.click_element(LocatorsOrderPage.BUTTON_NEXT)
        self.click_element(LocatorsOrderPage.DATA)
        data_locator = self.get_dynamic_locator(LocatorsOrderPage.DATA_PICKER_TEMPLATE, data)
        self.click_element(data_locator)
        self.click_element(LocatorsOrderPage.LENGTH_OF_RENT)
        rent_locator = self.get_dynamic_locator(LocatorsOrderPage.RENT_PICKER_TEMPLATE, rent)
        self.click_element(rent_locator)
        color_locator = self.get_dynamic_locator(LocatorsOrderPage.COLOR_PICKER_TEMPLATE, color)
        self.click_element(color_locator)
        self.add_text_to_element(LocatorsOrderPage.COMMENT, comment)
        self.click_element(LocatorsOrderPage.BUTTON_ACC_ORDER)
        self.click_element(LocatorsOrderPage.BUTTON_CONFIRMATION)


    @allure.step("Проверка отображения сообщения о заказе")
    def check_message(self):
        return self.find_element_with_wait(LocatorsOrderPage.ORDER_DONE).is_displayed()
