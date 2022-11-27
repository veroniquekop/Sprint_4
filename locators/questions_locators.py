from selenium.webdriver.common.by import By
class QuestionLocators:
    cookies_locator = (By.XPATH, "//*[contains(@class, 'App_CookieButton')]")

    question_1_locator = (By.XPATH, ".//div[@id ='accordion__heading-0']")
    accordion_answer_1_locator = (By.XPATH, ".//div[@id='accordion__panel-0']")
    answer_1_locator = (By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными')]")

    question_2_locator = (By.XPATH, ".//div[@id ='accordion__heading-1']")
    accordion_answer_2_locator = (By.XPATH, ".//div[@id='accordion__panel-1']")
    answer_2_locator = (By.XPATH, "//p[contains(text(), 'Пока что у нас так: один заказ — один самокат. Есл')]")

    question_3_locator = (By.XPATH, ".//div[@id ='accordion__heading-2']")
    accordion_answer_3_locator = (By.XPATH, ".//div[@id='accordion__panel-2']")
    answer_3_locator = (By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая. Мы привози')]")

    question_4_locator = (By.XPATH, ".//div[@id ='accordion__heading-3']")
    accordion_answer_4_locator = (By.XPATH, ".//div[@id='accordion__panel-3']")
    answer_4_locator = (By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня. Но скоро станем')]")

    question_5_locator = (By.XPATH, ".//div[@id ='accordion__heading-4']")
    accordion_answer_5_locator = (By.XPATH, ".//div[@id='accordion__panel-4']")
    answer_5_locator = (By.XPATH, "//p[contains(text(), 'Пока что нет! Но если что-то срочное — всегда можн')]")

    question_6_locator = (By.XPATH, ".//div[@id ='accordion__heading-5']")
    accordion_answer_6_locator = (By.XPATH, ".//div[@id='accordion__panel-5']")
    answer_6_locator = (By.XPATH, "//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой. Этого х')]")

    question_7_locator = (By.XPATH, ".//div[@id ='accordion__heading-6']")
    accordion_answer_7_locator = (By.XPATH, ".//div[@id='accordion__panel-6']")
    answer_7_locator = (By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет, объ')]")

    question_8_locator = (By.XPATH, ".//div[@id ='accordion__heading-7']")
    accordion_answer_8_locator = (By.XPATH, ".//div[@id='accordion__panel-7']")
    answer_8_locator = (By.XPATH, "//p[contains(text(), 'Да, обязательно. Всем самокатов! И Москве, и Моско')]")




