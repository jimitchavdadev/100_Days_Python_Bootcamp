from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the Chrome window open after execution

# Set the service using ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Initialize the webdriver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)


def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Ensure the page is loaded
    WebDriverWait(driver, 10).until(EC.title_is("Web form"))

    title = driver.title
    assert title == "Web form"

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()

    # Wait for the message to be displayed after form submission
    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message")))

    value = message.text
    assert value == "Received!"

    # Gracefully quit the browser session
    driver.quit()


test_eight_components()
