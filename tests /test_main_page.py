from pages.main_page import MainPage
import allure

class TestMainPage:
    @allure.title('Проверка переходов на сайте')
    def test_move_to_yandex_page(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_yandex().click()
        assert len(driver.window_handles) == 2

    def test_move_to_samokat_page(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.click_logo_samokat().click()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

