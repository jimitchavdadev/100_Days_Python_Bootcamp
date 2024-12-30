from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        # Twilio setup for SMS (you can change this to email if you prefer)
        self.account_sid = "YOUR_TWILIO_ACCOUNT_SID"
        self.auth_token = "YOUR_TWILIO_AUTH_TOKEN"
        self.client = Client(self.account_sid, self.auth_token)

        self.from_number = "YOUR_TWILIO_PHONE_NUMBER"
        self.to_number = "USER_PHONE_NUMBER"

    def send_notifications(self, flight_data):
        # Send a notification for each flight deal
        for flight in flight_data:
            message = f"Low Price Alert! Only {flight['price']} GBP to fly to {flight['city']} from London. " \
                      f"Departure: {flight['departure_date']}. More info: {flight['link']}"

            message_sent = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=self.to_number
            )
            print(f"Message sent: {message_sent.sid}")
