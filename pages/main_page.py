from locators.main_locators import MainLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_samokat(self):
        return self.driver.find_element(*MainLocators.samokat_logo_locator)
    def click_logo_yandex(self):
        return self.driver.find_element(*MainLocators.yandex_logo_locator)