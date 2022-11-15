from selenium import webdriver
from pages.main_page import MainPage

class TestMainPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/geckodriver")

    def test_move_to_yandex_page(self):
        main_page = MainPage(self.driver)
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_yandex().click()
        assert len(self.driver.window_handles) == 2

    def test_move_to_samokat_page(self):
        main_page = MainPage(self.driver)
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.click_logo_samokat().click()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()