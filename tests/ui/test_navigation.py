import pytest
from selenium import webdriver
from pages.navigation_page import NavigationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or any supported WebDriver
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigation_about(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.navigate_tabs()
