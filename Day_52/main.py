from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
INSTAGRAM_USERNAME = "your_instagram_username"  # Replace with your Instagram username
INSTAGRAM_PASSWORD = "your_instagram_password"  # Replace with your Instagram password
TARGET_ACCOUNT = "target_account_name"  # Replace with the target account username
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get(f"{INSTAGRAM_URL}accounts/login/")
        time.sleep(5)

        # Accept cookies if the pop-up appears
        try:
            accept_cookies = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]" )
            accept_cookies.click()
        except:
            pass

        # Enter login credentials
        username_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys(INSTAGRAM_USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(INSTAGRAM_PASSWORD)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)

        # Dismiss any save login info pop-up
        try:
            not_now_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")
            ))
            not_now_button.click()
        except:
            pass

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}{TARGET_ACCOUNT}/")
        time.sleep(5)

        followers_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "followers"))
        )
        followers_link.click()

        time.sleep(5)

        # Scroll through the followers popup
        followers_popup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']/div[2]")
        ))

        for _ in range(10):  # Adjust range for the number of scrolls
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Follow']")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)  # Wait to mimic human behavior
            except Exception as e:
                print("Error:", e)
                try:
                    cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                except:
                    pass

    def close_browser(self):
        self.driver.quit()

# Initialize the bot and execute the methods
bot = InstaFollower()
try:
    bot.login()
    bot.find_followers()
    bot.follow()
finally:
    bot.close_browser()
