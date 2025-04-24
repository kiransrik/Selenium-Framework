import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def chrome_options():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--window-size=1280,720")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options

@pytest.fixture(scope="function")
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1280, 720)
    yield driver
    driver.quit()
