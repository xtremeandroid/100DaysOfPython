import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from flight_data import FlightData
load_dotenv()


def get_dates():
    now = datetime.now()
    today = now.date()
    dates = {
        "tom_date": today + timedelta(days=1),
        "six_months_date": today + timedelta(days=6*30),
        "round_trip_7": today + timedelta(days=1) + timedelta(days=7),
        "round_trip_28": today + timedelta(days=1) + timedelta(days=28),
    }
    return dates


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        location_query_endpoint = "https://api.tequila.kiwi.com/locations/query"
        header = {
            "apiKey": os.getenv("KIWI_API_KEY")
        }
        params = {
            "term": city_name,
            "locale": "en-US",
            "limit": 10,
            "active_only": "true",
        }
        response = requests.get(location_query_endpoint, headers=header, params=params)
        response.raise_for_status()
        return response.json()["locations"][0]['code']

    def get_flight_details(self, fly_from, fly_to):
        flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {
            "apiKey": os.getenv("KIWI_API_KEY")
        }
        dates = get_dates()
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": dates["tom_date"],
            "date_to": dates["six_months_date"],
            "nights_in_dst_from": 30,
            "nights_in_dst_to": 45,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "partner_market": "in",
            "curr": "INR",
            "locale": "in",
        }
        response = requests.get(flight_search_endpoint, headers=header, params=params)
        response.raise_for_status()
        data = response.json()["data"][0]

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data


