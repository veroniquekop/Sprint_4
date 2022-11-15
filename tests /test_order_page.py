from selenium import webdriver
from pages.order_page import OrderPage

class TestOrderPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/geckodriver")

    def test_registration_button_up(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(self.driver)
        order_page.button_cookie_locator().click()
        order_page.button_order_up_locator().click()
        order_page.set_name("Бред")
        order_page.set_surname("Питт")
        order_page.set_address("Москва, Паршина, 10, кв 20")
        order_page.select_station_locator().click()
        order_page.select_list_of_stations_locator()
        order_page.set_station_one_locator().click()
        order_page.set_phone('79099909090')
        order_page.click_button_next_locator().click()
        order_page.set_date_locator().click()
        order_page.wait_for_load_datepicker_locator()
        order_page.select_datepicker()
        order_page.set_current_date().click()
        order_page.set_duration_locator().click()
        order_page.set_list_of_durations()
        order_page.set_current_duration().click()
        order_page.set_colour_black_locator().click()
        order_page.set_comment("Позвоните за 30 минут до доставки")
        order_page.click_button_confirm_locator().click()
        order_page.click_answer_yes_locator().click()
        order_page.check_status_of_order_locator()
        order_page.wait_for_load_status_locator()
        assert order_page.get_text_status() == 'Посмотреть статус'

    def test_registration_button_down(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(self.driver)
        order_page.button_order_down_locator().click()
        order_page.set_name("Анжелина")
        order_page.set_surname("Джоли")
        order_page.set_address("Москва, Живописная 12, кв 40")
        order_page.select_station_locator().click()
        order_page.select_list_of_stations_locator()
        order_page.set_station_two_locator().click()
        order_page.set_phone('79099901111')
        order_page.click_button_next_locator().click()
        order_page.set_date_locator().click()
        order_page.wait_for_load_datepicker_locator()
        order_page.select_datepicker()
        order_page.set_current_date2().click()
        order_page.set_duration_locator().click()
        order_page.set_list_of_durations()
        order_page.set_current_duration2().click()
        order_page.set_colour_grey_locator().click()
        order_page.set_comment("Звонок не работает, стучите")
        order_page.click_button_confirm_locator().click()
        order_page.click_answer_yes_locator().click()
        order_page.wait_for_load_status_locator()
        order_page.click_popup_status_button().click()
        assert 'track' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

