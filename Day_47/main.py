import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email and SMTP configuration
smtp_address = os.getenv("SMTP_ADDRESS")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

# Target price
target_price = 100.00

# URL of the product page
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Set up headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Make the request with headers
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the product title
title = soup.find("span", id="productTitle")
product_title = title.get_text().strip() if title else "Product Title Not Found"

# Extract the price
price = soup.find("span", class_="a-price-whole")
price_number = float(price.get_text().strip().replace(',', '')) if price else None

# Print the product title and price
print(f"Product Title: {product_title}")
if price_number:
    print(f"Price: ${price_number}")
else:
    print("Price not found.")

# If the price is below the target price, send an email
if price_number and price_number < target_price:
    buy_link = url  # Link to the product page

    # Compose the email
    subject = f"Price Alert! {product_title} is now ${price_number}"
    body = f"Good news! The price of {product_title} is now ${price_number}. You can buy it here: {buy_link}"

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_address, 587)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, email_address, msg.as_string())
        server.quit()
        print(f"Email sent! {product_title} is now ${price_number}")
    except Exception as e:
        print(f"Error sending email: {e}")
