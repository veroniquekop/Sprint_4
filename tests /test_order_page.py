from pages.order_page import OrderPage
import allure
class TestOrderPage:
    @allure.title('Проверка создания заказа')
    def test_registration_button_up(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.button_cookie_locator(driver).click()
        order_page.button_order_up_locator(driver).click()
        order_page.fill_register_fields("Бред", "Питт", "Москва, Паршина, 10, кв 20", '79099909090', driver)
        order_page.select_station_locator(driver).click()
        order_page.select_list_of_stations_locator(driver)
        order_page.set_station_one_locator(driver).click()
        order_page.click_button_next_locator(driver).click()
        order_page.set_date_locator(driver).click()
        order_page.wait_for_load_datepicker_locator(driver)
        order_page.select_datepicker(driver)
        order_page.set_current_date(driver).click()
        order_page.set_duration_locator(driver).click()
        order_page.set_list_of_durations(driver)
        order_page.set_current_duration(driver).click()
        order_page.set_colour_black_locator(driver).click()
        order_page.set_comment("Позвоните за 30 минут до доставки", driver)
        order_page.click_button_confirm_locator(driver).click()
        order_page.click_answer_yes_locator(driver).click()
        check_element = order_page.check_popup_status(driver).text
        number_of_order = check_element.split('Номер заказа:')[1].split('.')[0].strip()
        assert number_of_order.isnumeric()

    def test_registration_button_down(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.button_cookie_locator(driver).click()
        order_page.button_order_down_locator(driver).click()
        order_page.fill_register_fields("Анжелина", "Джоли", "Москва, Живописная 12, кв 40", '79099901111', driver)
        order_page.select_station_locator(driver).click()
        order_page.select_list_of_stations_locator(driver)
        order_page.set_station_two_locator(driver).click()
        order_page.click_button_next_locator(driver).click()
        order_page.set_date_locator(driver).click()
        order_page.wait_for_load_datepicker_locator(driver)
        order_page.select_datepicker(driver)
        order_page.set_current_date2(driver).click()
        order_page.set_duration_locator(driver).click()
        order_page.set_list_of_durations(driver)
        order_page.set_current_duration2(driver).click()
        order_page.set_colour_grey_locator(driver).click()
        order_page.set_comment("Звонок не работает, стучите", driver)
        order_page.click_button_confirm_locator(driver).click()
        order_page.click_answer_yes_locator(driver).click()
        order_page.wait_for_load_status_locator(driver)
        order_page.click_popup_status_button(driver).click()
        assert 'track' in driver.current_url



