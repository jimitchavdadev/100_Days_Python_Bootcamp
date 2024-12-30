from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests

# Constants
GOOGLE_FORM_URL = "your_google_form_url_here"  # Replace with your Google Form URL
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

class ZillowDataEntry:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def scrape_data(self):
        response = requests.get(ZILLOW_CLONE_URL, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        })
        soup = BeautifulSoup(response.text, "html.parser")

        self.links = [
            link.get("href") if link.get("href").startswith("http") else f"https://appbrewery.github.io{link.get('href')}"
            for link in soup.select(".list-card-top a")
        ]

        self.prices = [
            price.get_text().split("+")[0].strip() for price in soup.select(".list-card-price")
        ]

        self.addresses = [
            address.get_text().replace("\n", "").replace("|", "").strip()
            for address in soup.select(".list-card-addr")
        ]

    def fill_google_form(self):
        for address, price, link in zip(self.addresses, self.prices, self.links):
            self.driver.get(GOOGLE_FORM_URL)
            time.sleep(2)

            try:
                address_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @aria-label='Address']"))
                )
                address_input.send_keys(address)

                price_input = self.driver.find_element(By.XPATH, "//input[@type='text' and @aria-label='Price']")
                price_input.send_keys(price)

                link_input = self.driver.find_element(By.XPATH, "//input[@type='text' and @aria-label='Link']")
                link_input.send_keys(link)

                submit_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]")
                submit_button.click()

                time.sleep(2)  # Wait to mimic human behavior
            except Exception as e:
                print(f"Error submitting form for {address}: {e}")

    def close_browser(self):
        self.driver.quit()

# Main Execution
bot = ZillowDataEntry()
try:
    bot.scrape_data()
    bot.fill_google_form()
finally:
    bot.close_browser()
