from pages.order_page import OrderPage
import allure

class TestOrderPage:
    @allure.title('Проверка создания заказа')
    def test_registration_button_up(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.click_button_up()
        order_page.fill_register_fields("Бред", "Питт", "Москва, Паршина, 10, кв 20", '79099909090')
        order_page.select_station_1()
        order_page.click_button_next_locator().click()
        order_page.click_process_order_page_2()
        order_page.set_comment("Позвоните за 30 минут до доставки")
        order_page.click_confirm_buttons()
        check_element = order_page.check_popup_status().text
        number_of_order = check_element.split('Номер заказа:')[1].split('.')[0].strip()
        assert number_of_order.isnumeric()

    def test_registration_button_down(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrderPage(driver)
        order_page.click_button_down()
        order_page.fill_register_fields("Анжелина", "Джоли", "Москва, Живописная 12, кв 40", '79099901111')
        order_page.select_station_2()
        order_page.click_button_next_locator().click()
        order_page.click_process_order_page_set_2()
        order_page.set_comment("Звонок не работает, стучите")
        order_page.click_confirm_buttons_2()
        assert 'track' in driver.current_url



