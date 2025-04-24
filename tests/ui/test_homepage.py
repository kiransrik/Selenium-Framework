import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or any other browser driver
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage_loads_correctly(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.verify_homepage_title()
