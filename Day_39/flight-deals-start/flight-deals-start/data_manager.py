import os
import gspread
from google.oauth2.service_account import Credentials

class DataManager:
    def __init__(self):
        # Setup Google Sheets API credentials
        self.credentials = Credentials.from_service_account_file(
            'path/to/your/service/account/key.json', 
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open('Flight Deals').sheet1  # Modify sheet name accordingly

    def get_destinations(self):
        # Get the list of destinations from Google Sheets
        destinations_data = self.sheet.get_all_records()
        destinations = [data["City"] for data in destinations_data if data["City"]]
        return destinations

    def update_flight_data(self, flight_data):
        # Update Google Sheets with the flight details
        row = [flight_data["city"], flight_data["price"], flight_data["iata_code"], flight_data["departure_date"], flight_data["link"]]
        self.sheet.append_row(row)
