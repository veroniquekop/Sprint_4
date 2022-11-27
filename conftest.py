import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope='function')
def driver():
    firefox_options = Options()
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=firefox_options, executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/geckodriver")
    yield driver
    driver.quit()


