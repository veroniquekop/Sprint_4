from locators.order_locator import OrderLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    datepicker_locator = [By.XPATH, "//*[contains(@class, 'react-datepicker__month-container')]"]
    status_of_order = [By.XPATH, "//*[contains(@class, 'Order_Modal__YZ-d3')]"]

    def button_order_up_locator(self, driver):
        return self.driver.find_element(*OrderLocators.button_order_up_locator)
    def button_order_down_locator(self, driver):
        return self.driver.find_element(*OrderLocators.button_order_down_locator)
    def button_cookie_locator(self, driver):
        return self.driver.find_element(*OrderLocators.accept_cookies)
    def name_registration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.input_name_locator)
    def surname_registration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.input_surname_locator)
    def address_registration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.input_address_locator)
    def phone_registration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.input_phone_locator)
    def comment_registration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.comment_locator)
    def select_station_locator(self, driver):
        return self.driver.find_element(*OrderLocators.field_station_locator)
    def select_list_of_stations_locator(self, driver):
        return self.driver.find_element(*OrderLocators.list_of_stations)
    def set_station_one_locator(self, driver):
        return self.driver.find_element(*OrderLocators.station1_locator)
    def set_station_two_locator(self, driver):
        return self.driver.find_element(*OrderLocators.station2_locator)
    def click_button_next_locator(self, driver):
        return self.driver.find_element(*OrderLocators.button_next_locator)
    def set_date_locator(self, driver):
        return self.driver.find_element(*OrderLocators.select_date_button_locator)
    def wait_for_load_datepicker_locator(self, driver):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.datepicker_locator))
    def select_datepicker(self, driver):
        return self.driver.find_element(*OrderLocators.datepicker_locator)
    def set_current_date(self, driver):
        return self.driver.find_element(*OrderLocators.current_date_locator)
    def set_current_date2(self, driver):
        return self.driver.find_element(*OrderLocators.current_date2_locator)
    def set_duration_locator(self, driver):
        return self.driver.find_element(*OrderLocators.field_duration_locator)
    def set_list_of_durations(self, driver):
        return self.driver.find_element(*OrderLocators.list_of_durations)
    def set_current_duration(self, driver):
        return self.driver.find_element(*OrderLocators.current_duration_locator)
    def set_current_duration2(self, driver):
        return self.driver.find_element(*OrderLocators.current_duration2_locator)
    def set_colour_black_locator(self, driver):
        return self.driver.find_element(*OrderLocators.checkbox_colour_black_locator)
    def set_colour_grey_locator(self, driver):
        return self.driver.find_element(*OrderLocators.checkbox_colour_grey_locator)
    def click_button_confirm_locator(self, driver):
        return self.driver.find_element(*OrderLocators.confirm_order_button_locator)
    def wait_for_load_status_locator(self, driver):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.status_of_order))
    def click_popup_status_button(self, driver):
        return self.driver.find_element(*OrderLocators.successful_order_text_locator)
    def click_answer_yes_locator(self, driver):
        return self.driver.find_element(*OrderLocators.answer_yes_locator)
    def get_text_status(self, driver):
        return self.driver.find_element(*OrderLocators.successful_order_text_locator).text
    #def check_status_of_order_locator(self, driver):
        return self.driver.find_element(*OrderLocators.check_status_locator)
    def check_popup_status(self, driver):
        return self.driver.find_element(*OrderLocators.popup_locator)
    def set_name(self,name, driver):
        self.name_registration_locator(driver).send_keys(name)
    def set_surname(self,surname, driver):
        self.surname_registration_locator(driver).send_keys(surname)
    def set_address(self, address, driver):
        self.address_registration_locator(driver).send_keys(address)
    def set_phone(self, phone, driver):
        self.phone_registration_locator(driver).send_keys(phone)
    def set_comment(self, comment, driver):
        self.comment_registration_locator(driver).send_keys(comment)

    def fill_register_fields(self, name, surname, address, phone, driver):
        self.set_name(name, driver)
        self.set_surname(surname, driver)
        self.set_address(address, driver)
        self.set_phone(phone, driver)




