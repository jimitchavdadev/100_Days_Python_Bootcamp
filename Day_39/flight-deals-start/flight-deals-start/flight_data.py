class FlightData:
    def structure_flight_data(self, flight_details):
        # Structure the flight details into a more user-friendly format
        structured_data = []
        for flight in flight_details:
            flight_info = {
                "city": flight["city"],
                "price": flight["price"],
                "iata_code": flight["iata_code"],
                "departure_date": flight["departure_date"],
                "link": flight["link"]
            }
            structured_data.append(flight_info)
        return structured_data
