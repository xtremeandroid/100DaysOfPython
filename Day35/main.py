import requests
from twilio.rest import Client
# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
LAT = 19.0760
LON = 72.8777
API_OWM = "https://api.openweathermap.org/data/2.5/weather"
PARAMETERS = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}
will_rain = False


def send_sms(message_content):
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12184323195',
        body=message_content,
        to='+918737969494'
    )

    print(message.status)


response = requests.get(API_OWM, PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_code = weather_data['weather'][0]["id"]

if 600 > weather_code >= 500:
    will_rain = True

if will_rain:
    send_sms("Take an Umbrella, Before you go out !!")
else:
    send_sms("The weather looks clear Today")



