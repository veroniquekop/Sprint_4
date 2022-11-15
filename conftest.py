import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    driver = webdriver.Firefox(executable_path="/Users/veronikakopena/Desktop/qa_python_tasks-main/geckodriver")
    yield driver
    driver.quit()