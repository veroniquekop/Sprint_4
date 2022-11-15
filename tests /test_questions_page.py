from selenium import webdriver
from pages.questions_page import QuestionPage

class TestQuestionPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/geckodriver")

    def test_question_1_form(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page = QuestionPage(self.driver)
        question_page.accept_cookies().click()
        question_page.get_question1().click()
        question_page.get_answer1_from_accordion().click()
        answer1 = question_page.get_text_answer1()
        assert answer1 == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_question_2_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question2().click()
        question_page.get_answer2_from_accordion().click()
        answer2 = question_page.get_text_answer2()
        assert answer2 == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_question_3_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question3().click()
        question_page.get_answer3_from_accordion().click()
        answer3 = question_page.get_text_answer3()
        assert answer3 == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_question_4_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question4().click()
        question_page.get_answer4_from_accordion().click()
        answer4 = question_page.get_text_answer4()
        assert answer4 == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_question_5_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question5().click()
        question_page.get_answer5_from_accordion().click()
        answer5 = question_page.get_text_answer5()
        assert answer5 == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_question_6_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question6().click()
        question_page.get_answer6_from_accordion().click()
        answer6 = question_page.get_text_answer6()
        assert answer6 == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_question_7_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question7().click()
        question_page.get_answer7_from_accordion().click()
        answer7 = question_page.get_text_answer7()
        assert answer7 == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_question_8_form(self):
        question_page = QuestionPage(self.driver)
        question_page.get_question8().click()
        question_page.get_answer8_from_accordion().click()
        answer8 = question_page.get_text_answer8()
        assert answer8 == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardom_class(cls):
        cls.driver.quit()
