from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from utils import config

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def load(self):
        self.driver.get(config.BASE_URL)
        time.sleep(2)  # Wait for the page to load
        title = self.driver.title
        filename = f"screenshots/{title.lower().replace(' ', '_')}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(filename)

    def verify_homepage_title(self):
        assert "Guru99" in self.driver.title, "Homepage title did not match"
        elements = self.driver.find_elements(By.XPATH, "//*[text()='NonExistentElement']")
        assert len(elements) == 0, "Unexpected element found!"
