from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

def main():
    # Initialize all classes
    data_manager = DataManager()
    flight_search = FlightSearch()
    flight_data = FlightData()
    notification_manager = NotificationManager()

    # Get destinations from Google Sheets
    destinations = data_manager.get_destinations()

    # Search for flights
    flight_details = flight_search.search_flights(destinations)

    # Structure the flight data
    structured_flight_data = flight_data.structure_flight_data(flight_details)

    # Notify the user about the flight deals
    notification_manager.send_notifications(structured_flight_data)


if __name__ == "__main__":
    main()
