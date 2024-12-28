import allure
import pytest
from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import UrlsList, OrderData1, OrderData2

@pytest.mark.parametrize("order_data", [OrderData1])
@allure.title("Заказ самоката через верхнюю кнопку")
def test_fill_order_form_data1(driver, order_data):
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    home_page.open_url(UrlsList.home)
    home_page.close_banner()
    home_page.scroll_to_order_button("top")
    home_page.click_order_button("top")
    order_page.fill_order_form(
        first_name=order_data.first_name,
        last_name=order_data.last_name,
        address=order_data.address,
        phone=order_data.telephone_number,
        metro=order_data.metro_station,
        rent=order_data.rent_duration,
        color=order_data.color_skate,
        data=order_data.date_delivered,
        comment=order_data.comment
    )
    order_page.check_message()
    assert order_page.check_message()

@pytest.mark.parametrize("order_data", [OrderData2])
@allure.title("Заказ самоката через верхнюю кнопку")
def test_fill_order_form_data2(driver, order_data):
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    home_page.open_url(UrlsList.home)
    home_page.close_banner()
    home_page.scroll_to_order_button("bottom")
    home_page.click_order_button("bottom")
    order_page.fill_order_form(
        first_name=order_data.first_name,
        last_name=order_data.last_name,
        address=order_data.address,
        phone=order_data.telephone_number,
        metro=order_data.metro_station,
        rent=order_data.rent_duration,
        color=order_data.color_skate,
        data=order_data.date_delivered,
        comment=order_data.comment
    )
    order_page.check_message()
    assert order_page.check_message()