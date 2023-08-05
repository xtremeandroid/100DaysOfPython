from flight_search import FlightSearch
import requests
# pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/55213f18f7194b4bf5112d22c435f9f4/100DaysOfPythonFlightDeals/prices"
        self.headers = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }
        self.sheet_data = ''

    def get_data(self):
        response = requests.get(self.SHEETY_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def add_data(self, row_id, data):
        data_to_add = {
            "price": {
                "iataCode": data
            }
        }
        response = requests.put(f"{self.SHEETY_ENDPOINT}/{row_id}", headers=self.headers, json=data_to_add)
        response.raise_for_status()
        # print(response.json())