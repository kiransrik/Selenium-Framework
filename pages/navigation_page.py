from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from utils import config

class NavigationPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def navigate_tabs(self):
        self.driver.get(config.BASE_URL)
        wait = WebDriverWait(self.driver, 10)

        # Click the "Selenium" dropdown
        selenium_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Selenium")))
        selenium_menu.click()

        # Menu items and expected titles
        menu_items = {
            "Flash Movie Demo": "Flash Movie Demo",
            "Radio & Checkbox Demo": "Radio Button & Check Box Demo",
            "Table Demo": "Table Demo"
        }

        for item_text, expected_page_title in menu_items.items():
            # Wait for item and click
            menu_item = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, item_text)))
            menu_item.click()

            # Wait for title to load and verify
            wait.until(EC.title_is(expected_page_title))
            assert self.driver.title == expected_page_title, \
                f"Title mismatch for {item_text}! Expected: {expected_page_title}, Found: {self.driver.title}"

            # Screenshot
            os.makedirs("screenshots", exist_ok=True)
            filename = f"screenshots/{item_text.lower().replace(' ', '_')}.png"
            self.driver.save_screenshot(filename)

            # Reopen the Selenium dropdown for the next item
            selenium_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Selenium")))
            selenium_menu.click()