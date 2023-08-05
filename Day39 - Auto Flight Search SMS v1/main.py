# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_data()

for item in sheet_data:
    if not item['iataCode']:
        data = flight_search.get_destination_code(item["city"])
        data_manager.add_data(item['id'], data)

    fare_data = flight_search.get_flight_details("BOM", item["iataCode"])

    if fare_data.price <= item['lowestPrice']:
        message = (f"Low price alert! Only ₹{fare_data.price} to fly from {fare_data.origin_city}-{fare_data.origin_airport} to "
                   f"{fare_data.destination_city}-{fare_data.destination_airport}, from {fare_data.out_date} to {fare_data.return_date}.")
        nm = NotificationManager()
        nm.send_sms(message)




