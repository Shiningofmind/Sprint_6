from selenium.webdriver.common.by import By

class LocatorsHomePage:
    #кнопки
    ORDER_BUTTON_1 = By.XPATH, '//*[contains(@class, "Button_Button__ra12g") and text()="Заказать"]' #кнопка заказа в шапке страницы
    ORDER_BUTTON_2 = By.XPATH,'//*[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]' #кнопка заказа внизу страницы

    #лого
    LOGO_YANDEX = By.XPATH,'//*[contains(@class, "Header_LogoYandex__3TSOI")]' #логотип Яндекса ведущий на Дзен
    LOGO_SCOOTER = By.XPATH,'//*[contains(@class, "Header_LogoScooter__3lsAR")]' #логотип Яндекс самоката
    LOGO_DZEN = By.XPATH,'//*[contains(@class, "dzen-layout--desktop-base-header__logoWithText-3k")]' #логотип Яндекс Дзен
    HEADER = By.XPATH,'//*[contains(@class, "Home_Header__iJKdX")]'
    POPUP_BUTTON = [By.XPATH, "//button[contains(text(),'да все привыкли')]"]
    #выпадающие списки
    QUESTION_LOCATOR = By.XPATH,'//*[@id="accordion__heading-{}"]' #Вопрос секции FAQ
    ANSWER_LOCATOR = By.XPATH,'//*[@id="accordion__panel-{}"]' #Ответ секции FAQ
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]' #Скролл до последнего вопроса
    SPOILER_FAQ_LAST = (By.XPATH, '//*[contains(@class,"accordion__item")][last()]')
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@id="accordion__heading-7"]'  # Вопрос восьмой секции FAQ

