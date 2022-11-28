from locators.order_locator import OrderLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    datepicker_locator = [By.XPATH, "//*[contains(@class, 'react-datepicker__month-container')]"]
    status_of_order = [By.XPATH, "//*[contains(@class, 'Order_Modal')]"]
    check_button_down = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]
    field_station_locator = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    station1_locator = [By.XPATH, ".//*[@data-index='1']"]  # Станция 1
    list_of_stations = [By.XPATH, "//*[contains(@class, 'select-search')]"]
    input_name_locator = [By.XPATH, "//input[@placeholder='* Имя']"]
    wait_when_samokat = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    def button_order_up_locator(self):
        return self.driver.find_element(*OrderLocators.button_order_up_locator)
    def wait_button_order_down(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.check_button_down))
    def wait_select_station_locator(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.field_station_locator))
    def wait_select_station_1(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.station1_locator))
    def wait_name_locator(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.input_name_locator))
    def wait_when_samokat(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.wait_when_samokat))
    def button_order_down(self):
        return self.driver.find_element(*OrderLocators.button_order_down_locator)
    def button_cookie_locator(self):
        return self.driver.find_element(*OrderLocators.accept_cookies)
    def name_registration_locator(self):
        return self.driver.find_element(*OrderLocators.input_name_locator)
    def surname_registration_locator(self):
        return self.driver.find_element(*OrderLocators.input_surname_locator)
    def address_registration_locator(self):
        return self.driver.find_element(*OrderLocators.input_address_locator)
    def phone_registration_locator(self):
        return self.driver.find_element(*OrderLocators.input_phone_locator)
    def comment_registration_locator(self):
        return self.driver.find_element(*OrderLocators.comment_locator)
    def select_station_locator(self):
        return self.driver.find_element(*OrderLocators.field_station_locator)
    def select_list_of_stations_locator(self):
        return self.driver.find_element(*OrderLocators.list_of_stations)
    def set_station_one_locator(self):
        return self.driver.find_element(*OrderLocators.station1_locator)
    def set_station_two_locator(self):
        return self.driver.find_element(*OrderLocators.station2_locator)
    def click_button_next_locator(self):
        return self.driver.find_element(*OrderLocators.button_next_locator)
    def set_date_locator(self):
        return self.driver.find_element(*OrderLocators.select_date_button_locator)
    def wait_for_load_datepicker_locator(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.datepicker_locator))
    def select_datepicker(self):
        return self.driver.find_element(*OrderLocators.datepicker_locator)
    def set_current_date(self):
        return self.driver.find_element(*OrderLocators.current_date_locator)
    def set_current_date2(self):
        return self.driver.find_element(*OrderLocators.current_date2_locator)
    def set_duration_locator(self):
        return self.driver.find_element(*OrderLocators.field_duration_locator)
    def set_list_of_durations(self):
        return self.driver.find_element(*OrderLocators.list_of_durations)
    def set_current_duration(self):
        return self.driver.find_element(*OrderLocators.current_duration_locator)
    def set_current_duration2(self):
        return self.driver.find_element(*OrderLocators.current_duration2_locator)
    def set_colour_black_locator(self):
        return self.driver.find_element(*OrderLocators.checkbox_colour_black_locator)
    def set_colour_grey_locator(self):
        return self.driver.find_element(*OrderLocators.checkbox_colour_grey_locator)
    def click_button_confirm_locator(self):
        return self.driver.find_element(*OrderLocators.confirm_order_button_locator)
    def click_popup_status_button(self):
        return self.driver.find_element(*OrderLocators.successful_order_text_locator)
    def click_answer_yes_locator(self):
        return self.driver.find_element(*OrderLocators.answer_yes_locator)
    def get_text_status(self):
        return self.driver.find_element(*OrderLocators.successful_order_text_locator).text
    def check_popup_status(self):
        return self.driver.find_element(*OrderLocators.popup_locator)
    def set_name(self,name):
        self.name_registration_locator().send_keys(name)
    def set_surname(self,surname):
        self.surname_registration_locator().send_keys(surname)
    def set_address(self, address):
        self.address_registration_locator().send_keys(address)
    def set_phone(self, phone):
        self.phone_registration_locator().send_keys(phone)
    def set_comment(self, comment):
        self.comment_registration_locator().send_keys(comment)

    def fill_register_fields(self, name, surname, address, phone):
        return self.set_name(name), self.set_surname(surname), self.set_address(address), self.set_phone(phone)
    def click_button_up(self):
        return self.button_cookie_locator().click(), self.button_order_up_locator().click()
    def select_station_1(self):
        return self.select_station_locator().click(), self.select_list_of_stations_locator(), self.set_station_one_locator().click()
    def click_process_order_page_2(self):
        return self.set_date_locator().click(), self.wait_for_load_datepicker_locator(), self.select_datepicker(), self.set_current_date().click(), self.set_duration_locator().click(), self.set_list_of_durations(), self.set_current_duration().click(),  self.set_colour_black_locator().click()
    def click_confirm_buttons(self):
        return self.click_button_confirm_locator().click(), self.click_answer_yes_locator().click(), self.check_popup_status()

    def click_button_down(self):
        return self.button_cookie_locator().click(), self.wait_button_order_down(), self.button_order_down().click()
    def select_station_2(self):
        return self.select_station_locator().click(), self.select_list_of_stations_locator(), self.set_station_two_locator().click()
    def click_process_order_page_set_2(self):
        return self.set_date_locator().click(), self.wait_for_load_datepicker_locator(), self.select_datepicker(), self.set_current_date2().click(), self.set_duration_locator().click(), self.set_list_of_durations(), self.set_current_duration2().click(), self.set_colour_grey_locator().click()
    def click_confirm_buttons_2(self):
        return self.click_button_confirm_locator().click(), self.click_answer_yes_locator().click(), self.click_popup_status_button().click()