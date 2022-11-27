from selenium.webdriver.common.by import By
class OrderLocators:
    button_order_up_locator = (By.XPATH, "//*[contains(@class, 'Button_Button')][1]")  # Кнопка 'Заказать' (сверху)
    button_order_down_locator = (By.XPATH, "//*[contains(@class, 'Button_Middle')]") # Кнопка 'Заказать' (снизу)
    accept_cookies = (By.XPATH, "//*[contains(@class, 'App_CookieButton')]") # Кнопка 'Принять куки'
    input_name_locator = (By.XPATH, "//input[@placeholder='* Имя']") #Ввод имени
    input_surname_locator = (By.XPATH, "//input[@placeholder='* Фамилия']") #Ввод фамилии
    input_address_locator = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    field_station_locator = (By.XPATH, "//input[@placeholder='* Станция метро']") #Поле станция
    list_of_stations = (By.XPATH, "//*[contains(@class, 'select-search')]") #Список станций
    station1_locator = (By.XPATH, ".//*[@data-index='1']") #Станция 1
    station2_locator = (By.XPATH, ".//*[@data-index='2']") #Станция 2
    input_phone_locator = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") #Ввод телефона
    button_next_locator = (By.XPATH, "//*[contains(@class, 'Button_Middle')]") #Кнопка Далее
    select_date_button_locator = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") #Кнопка выбора даты
    datepicker_locator = (By.XPATH, "//*[contains(@class, 'react-datepicker__month-container')]") #Указатель даты
    current_date_locator = (By.XPATH, "// *[contains(@class, 'react-datepicker__day--030')]") #Указатъ конкретную дату
    current_date2_locator = (By.XPATH, "// *[contains(@class, 'react-datepicker__day--020')]")  # Указатъ конкретную дату
    field_duration_locator = (By.XPATH, "//*[contains(@class, 'Dropdown-root')]")  # Срок аренды
    list_of_durations = (By.XPATH, "//*[contains(@class, 'Dropdown-menu')]") # Список периодов аренды
    current_duration_locator = (By.XPATH, "//*[contains(text(),'двое суток')]")  #Определенный срок аренды - 2 суток
    current_duration2_locator = (By.XPATH, "//*[contains(text(),'трое суток')]")  # Определенный срок аренды - 3 суток
    checkbox_colour_black_locator = (By.XPATH, "//*[contains(@class, 'Checkbox_Input')][1]")  # Чекбокс 'Выбрать цвет' (чёрный)
    checkbox_colour_grey_locator = (By.XPATH, "//label[contains(text(),'серая безысходность')]")  # Чекбокс 'Выбрать цвет' (серый)
    comment_locator = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  #Комментарий к курьеру
    confirm_order_button_locator = (By.XPATH, "//*[contains(@class, 'Button_Button__ra12g Button_Middle')][2]")  # Подтвердить заказ
    popup_locator = (By.XPATH, "//*[contains(@class, 'Order_Modal')]")  # попап "Статус заказа"
    successful_order_text_locator = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
    answer_yes_locator = (By.XPATH, "//*[contains(text(),'Да')]") #попап "Да"
    popup_status_locator = (By.XPATH, "//*[contains(@class, 'Order_Modal')][4]")  # попап "статус"
    check_status_locator = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]") # попап "посмотреть статус"

