from pages.questions_page import QuestionPage
import allure
class TestQuestionPage:
    @allure.title('Проверка открытия вопросов')
    def test_question_1_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question1(driver).click()
        question_page.get_answer1_from_accordion(driver).click()
        answer1 = question_page.get_text_answer1(driver)
        assert answer1 == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_question_2_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question2(driver).click()
        question_page.get_answer2_from_accordion(driver).click()
        answer2 = question_page.get_text_answer2(driver)
        assert answer2 == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_question_3_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question3(driver).click()
        question_page.get_answer3_from_accordion(driver).click()
        answer3 = question_page.get_text_answer3(driver)
        assert answer3 == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_question_4_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question4(driver).click()
        question_page.get_answer4_from_accordion(driver).click()
        answer4 = question_page.get_text_answer4(driver)
        assert answer4 == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_question_5_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question5(driver).click()
        question_page.get_answer5_from_accordion(driver).click()
        answer5 = question_page.get_text_answer5(driver)
        assert answer5 == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_question_6_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question6(driver).click()
        question_page.get_answer6_from_accordion(driver).click()
        answer6 = question_page.get_text_answer6(driver)
        assert answer6 == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_question_7_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question7(driver).click()
        question_page.get_answer7_from_accordion(driver).click()
        answer7 = question_page.get_text_answer7(driver)
        assert answer7 == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_question_8_form(self, driver):
        question_page = QuestionPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page.accept_cookies(driver).click()
        question_page.get_question8(driver).click()
        question_page.get_answer8_from_accordion(driver).click()
        answer8 = question_page.get_text_answer8(driver)
        assert answer8 == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

