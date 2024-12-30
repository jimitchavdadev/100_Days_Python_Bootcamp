from datetime import datetime
import pandas
import random
from smtplib import SMTP

# Replace with your actual email and password
MY_EMAIL = ""
MY_PASSWORD = ""  # Use app password if 2FA is enabled

# Today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays CSV file
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Choose a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Read letter template and replace placeholder
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the email
    with SMTP("smtp.gmail.com") as connection:  # Using Gmail's SMTP server
        connection.starttls()  # Start TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login with your email and app password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"  # Subject and body of the email
        )
