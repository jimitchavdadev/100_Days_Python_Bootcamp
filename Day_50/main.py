from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
TINDER_URL = "https://tinder.com/"
FACEBOOK_EMAIL = "your_facebook_email@example.com"  # Replace with your Facebook email
FACEBOOK_PASSWORD = "your_facebook_password"        # Replace with your Facebook password

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open Tinder and Click on Login
    driver.get(TINDER_URL)
    time.sleep(5)  # Wait for the page to load

    login_button = driver.find_element(By.XPATH, '//a[contains(text(), "Log in")]')
    login_button.click()
    time.sleep(2)

    fb_login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login with Facebook")]')
    fb_login_button.click()
    time.sleep(5)

    # Step 2: Switch to Facebook Login Window
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)

    # Step 3: Log in to Facebook
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(FACEBOOK_EMAIL)

    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(FACEBOOK_PASSWORD)

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(5)

    # Step 4: Switch back to Tinder Window
    driver.switch_to.window(base_window)
    time.sleep(5)

    # Step 5: Dismiss Pop-ups
    try:
        location_allow = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Allow")]'))
        )
        location_allow.click()
    except Exception:
        pass

    try:
        notifications_dismiss = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not interested")]'))
        )
        notifications_dismiss.click()
    except Exception:
        pass

    try:
        cookies_accept = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "I Accept")]'))
        )
        cookies_accept.click()
    except Exception:
        pass

    # Step 6: Like Profiles
    while True:
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Like"]'))
            )
            like_button.click()
            time.sleep(2)  # Delay between likes
        except Exception as e:
            print(f"Encountered exception: {e}")

            try:
                match_popup = driver.find_element(By.XPATH, '//button[contains(text(), "Back to Tinder")]')
                match_popup.click()
                time.sleep(2)
            except Exception:
                print("No match popup found, retrying...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up
    driver.quit()
