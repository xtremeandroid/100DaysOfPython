import requests
from datetime import datetime
# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()
N_APP_ID = os.getenv("N_APP_ID")
N_API_KEY = os.getenv("N_API_KEY")


def get_query_processes():
    nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    query = {
        "query": input("Enter The Exercises you did : ")
    }
    headers = {
        "x-app-id": N_APP_ID,
        "x-app-key": N_API_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(nutritionix_exercise_endpoint, headers=headers, json=query)
    response.raise_for_status()
    return response.json()


# data = get_query_processes()

def add_data_to_sheets():
    data = get_query_processes()
    user_data = data['exercises'][0]
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d/%m/%Y")
    sheety_api_endpoint = "https://api.sheety.co/55213f18f7194b4bf5112d22c435f9f4/100DaysOfPythonMyWorkouts/workouts"
    headers = {
        "Authorization": os.getenv("SHEETY_AUTH")
    }
    exercise_data = {
        "workout": {
            "date": date_str,
            "time": time_str,
            "exercise": user_data['name'].title(),
            "duration": user_data['duration_min'],
            "calories": user_data['nf_calories'],
        }
    }

    # Get Data
    # response = requests.get(sheety_api_endpoint, headers=headers)
    # response.raise_for_status()
    # print(response.json())

    # Add Data
    response = requests.post(sheety_api_endpoint, headers=headers, json=exercise_data)
    response.raise_for_status()
    print(response.text)


add_data_to_sheets()

