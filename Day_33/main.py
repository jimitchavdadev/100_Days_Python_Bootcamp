import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = ""
MY_PASSWORD = ""  # Use app password if 2FA is enabled
MY_LAT = 51.507351  # Your latitude (London)
MY_LONG = -0.127758  # Your longitude (London)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise error if status is not 200
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise error if status is not 200
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    time.sleep(60)  # Check every minute
    if is_iss_overhead() and is_night():
        # If both conditions are met, send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:  # Corrected to use Gmail's SMTP server
            connection.starttls()  # Start TLS encryption
            connection.login(MY_EMAIL, MY_PASSWORD)  # Log in with your email and app password
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up👆\n\nThe ISS is above you in the sky."
            )
