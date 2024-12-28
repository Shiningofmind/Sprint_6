from selenium.webdriver.common.by import By

class LocatorsOrderPage:

    #поля ввода
    NAME_INPUT_FIELD = By.XPATH, '//*[@placeholder="* Имя"]' #поле ввода имени
    SURNAME_INPUT_FIELD = By.XPATH, '//*[@placeholder="* Фамилия"]' #поле ввода фамилии
    ADDRESS_INPUT_FIELD = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]' #поле ввода адреса
    PHONE_INPUT_FIELD = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]' #поле ввода  телефона
    COMMENT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]' #поле ввода комментария
    
    #выпадающие списки
    METRO = By.XPATH, '//*[@placeholder="* Станция метро"]'  # вызов выпадающего календаря
    METRO_STATION_TEMPLATE = (By.XPATH, './/*[contains(text(), "{}")]')
    FIRST_METRO_STATION = By.XPATH, './/*[contains(text(), "Лужники")]' #станция метро из выпадающего списка
    SECOND_METRO_STATION = By.XPATH, './/*[contains(text(), "Спортивная")]' #станция метро из выпадающего списка
    DATA = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]' #вызов выпадающего календаря
    DATA_PICKER_TEMPLATE = By.XPATH, '//div[contains(@aria-label, "{}")]'  # выбор даты доставки
    DATA_PICKER = By.XPATH, '//div[@aria-label="Choose вторник, 31-е декабря 2024 г."]' #выбор даты доставки
    LENGTH_OF_RENT = By.XPATH, '//*[contains(@class, "Dropdown-root")]' #вызов списка выбора длительности аренды
    RENT_PICKER_TEMPLATE = By.XPATH, '//*[contains(@class, "Dropdown-option") and text()="{}"]'  # Шаблон для длительности аренды
    RENT_PICKER = By.XPATH, '//*[contains(@class, "Dropdown-option") and text()="трое суток"]' #выбор длительности аренды
    
    
    
    #кнопки
    BUTTON_NEXT = By.XPATH, '//*[contains(@class, "Button_Middle__1CSJM") and text()="Далее"]' #кнопка "Далее"
    BUTTON_ACC_ORDER = By.XPATH, '//*[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]' #кнопка "Заказать"
    BUTTON_CONFIRMATION = By.XPATH, '//*[contains(@class, "Button_Button__ra12g") and text()="Да"]' #кнопка подтверждения заказа
    BUTTON_REJECTION = By.XPATH, '//*[contains(@class, "Button_Button__ra12g") and text()="Нет"]' #кнопка отказа от заказа
    
    #чекбоксы
    COLOR_PICKER_TEMPLATE = (By.XPATH, '//*[contains(@id, "{}")]')  # Шаблон для чек-боксов цвета
    BLACK_COLOR = By.XPATH, '//*[contains(@id, "black")]' #чек-бокс с черным самокатом
    GREY_COLOR = By.XPATH, '//*[contains(@id, "grey")]' #чек-бокс с серым самокатом
    
    ORDER_DONE = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]' #надпись всплывающего окна успешного заказа