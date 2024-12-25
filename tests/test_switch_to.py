import allure
from data import UrlsList
from pages.home_page import HomePage

class TestSwitchTo:

    @allure.title("Проверка логотипа Яндекса")
    def test_switch_to_yandex(self, driver):
        main_page = HomePage(driver)
        main_page.open_url(UrlsList.home)
        main_page.close_banner()
        main_page.click_yandex_logo()
        main_page.switch_to_window(1)
        assert main_page.is_dzen_logo_displayed(), "Логотип Дзен не отображается или URL неправильный."

    @allure.title("Проверка логотипа Самоката")
    def test_switch_to_scooter(self, driver):
        main_page = HomePage(driver)
        main_page.open_url(UrlsList.home)
        main_page.close_banner()
        main_page.click_scooter_logo()
        assert main_page.is_scooter_header_displayed(), "Заголовок Самокат не отображается или URL неправильный."