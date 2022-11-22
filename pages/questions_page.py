from locators.questions_locators import QuestionLocators
from selenium.webdriver.common.by import By

class QuestionPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        return self.driver.find_element(*QuestionLocators.cookies_locator)

    def move_to_question1_from(self):
        question1 = [By.XPATH, ".//div[@id ='accordion__heading-0']"]
        return self.driver.execute_script("arguments[0].scrollIntoView();", question1)
    def get_question1(self):
        return self.driver.find_element(*QuestionLocators.question_1_locator)
    def get_answer1_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_1_locator)
    def get_text_answer1(self):
        return self.driver.find_element(*QuestionLocators.answer_1_locator).text

    def get_question2(self):
        return self.driver.find_element(*QuestionLocators.question_2_locator)
    def get_answer2_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_2_locator)
    def get_text_answer2(self):
        return self.driver.find_element(*QuestionLocators.answer_2_locator).text

    def get_question3(self):
        return self.driver.find_element(*QuestionLocators.question_3_locator)
    def get_answer3_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_3_locator)
    def get_text_answer3(self):
        return self.driver.find_element(*QuestionLocators.answer_3_locator).text

    def get_question4(self):
        return self.driver.find_element(*QuestionLocators.question_4_locator)
    def get_answer4_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_4_locator)
    def get_text_answer4(self):
        return self.driver.find_element(*QuestionLocators.answer_4_locator).text

    def get_question5(self):
        return self.driver.find_element(*QuestionLocators.question_5_locator)
    def get_answer5_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_5_locator)
    def get_text_answer5(self):
        return self.driver.find_element(*QuestionLocators.answer_5_locator).text

    def get_question6(self):
        return self.driver.find_element(*QuestionLocators.question_6_locator)
    def get_answer6_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_6_locator)
    def get_text_answer6(self):
        return self.driver.find_element(*QuestionLocators.answer_6_locator).text

    def get_question7(self):
        return self.driver.find_element(*QuestionLocators.question_7_locator)
    def get_answer7_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_7_locator)
    def get_text_answer7(self):
        return self.driver.find_element(*QuestionLocators.answer_7_locator).text

    def get_question8(self):
        return self.driver.find_element(*QuestionLocators.question_8_locator)
    def get_answer8_from_accordion(self):
        return self.driver.find_element(*QuestionLocators.accordion_answer_8_locator)
    def get_text_answer8(self):
        return self.driver.find_element(*QuestionLocators.answer_8_locator).text




