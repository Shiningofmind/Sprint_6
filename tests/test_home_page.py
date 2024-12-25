import allure
import pytest
from data import QUESTIONS_AND_ANSWERS, UrlsList
from pages.home_page import HomePage


class TestHomePage:
    @pytest.mark.parametrize('num, result', QUESTIONS_AND_ANSWERS)
    @allure.title("Тестирование выпадающего списка")
    def test_questions_and_answers(self, driver, num, result):
        home_page = HomePage(driver)
        home_page.open_url(UrlsList.home)
        home_page.close_banner()
        actual_result = home_page.get_answer_text(num)
        assert actual_result == result, f"Для вопроса {num} ожидался ответ '{result}', но получен '{actual_result}'"


