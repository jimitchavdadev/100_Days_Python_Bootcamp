import requests
from twilio.rest import Client
import datetime

# OpenWeatherMap API setup
API_KEY = ''
LATITUDE = ''  # Example: '37.7749'
LONGITUDE = ''  # Example: '-122.4194'
URL = f'http://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&units=metric&appid={API_KEY}'

# Twilio setup
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
FROM_PHONE = ''
TO_PHONE = ''


# Function to check if it will rain in the next 12 hours
def will_it_rain():
    response = requests.get(URL)
    data = response.json()

    # Get the forecast for the next 12 hours
    forecast = data['list']

    # Check if there is rain in the next 12 hours
    for item in forecast:
        # Check if there's rain in the forecast data
        if 'rain' in item:
            rain_volume = item['rain'].get('3h', 0)
            if rain_volume > 0:
                return True
    return False


# Function to send SMS using Twilio
def send_sms():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It will rain in the next 12 hours! Stay dry.",
        from_=FROM_PHONE,
        to=TO_PHONE
    )
    print(f"SMS sent to {TO_PHONE}: {message.sid}")


# Main function
def main():
    if will_it_rain():
        send_sms()
    else:
        print("No rain expected in the next 12 hours.")


if __name__ == "__main__":
    main()
