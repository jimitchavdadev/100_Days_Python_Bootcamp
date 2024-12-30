from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
PROMISED_DOWN = 150  # Mbps
PROMISED_UP = 10  # Mbps
TWITTER_EMAIL = "your_twitter_email@example.com"  # Replace with your Twitter email
TWITTER_PASSWORD = "your_twitter_password"         # Replace with your Twitter password
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        time.sleep(5)  # Wait for the page to load

        # Start the speed test
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        # Wait for the test to complete
        time.sleep(60)  # Adjust based on your connection speed

        # Retrieve download and upload speeds
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print(f"Download Speed: {self.down} Mbps")
        print(f"Upload Speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)

        # Log in to Twitter
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)

        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

        # Compose a tweet
        tweet_text = (f"Hey ISP, why is my internet speed {self.down} Mbps down / {self.up} Mbps up
"
                      f"when I am paying for {PROMISED_DOWN} Mbps down / {PROMISED_UP} Mbps up?")

        tweet_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']"))
        )
        tweet_box.send_keys(tweet_text)

        # Send the tweet
        tweet_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]'))
        )
        tweet_button.click()
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()

# Initialize the bot and execute the methods
bot = InternetSpeedTwitterBot()
try:
    bot.get_internet_speed()
    bot.tweet_at_provider()
finally:
    bot.close_browser()