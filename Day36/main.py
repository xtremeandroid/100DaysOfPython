import itertools
import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
STOCK = "RELIANCE.BSE"
COMPANY_NAME = "Reliance"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "full",
    "apikey": os.getenv("AV_API_KEY"),
}

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_PARAMS = {
    'q': COMPANY_NAME,
    'sortBy': 'publishedAt',
    'apiKey': os.getenv("NEWS_API_KEY"),
    'pageSize': 3,
}
top_articles = []


def check_stock_movement():
    response = requests.get(STOCK_API_ENDPOINT, STOCK_API_PARAMS)
    response.raise_for_status()
    stock_data = response.json()
    daily_stock_data = stock_data["Time Series (Daily)"]
    res = dict(itertools.islice(daily_stock_data.items(), 2))
    date1 = list(res.keys())[0]
    today_stock_data = res[date1]
    date2 = list(res.keys())[1]
    yesterday_stock_data = res[date2]

    today_open = float(today_stock_data['1. open'])
    yesterday_close = float(yesterday_stock_data['4. close'])
    percentage_change = ((today_open - yesterday_close) / yesterday_close) * 100
    if percentage_change > 2:
        get_news()
        message_content = (f"{COMPANY_NAME}: 🔺2% Headline : {top_articles[0]['title']}."
                       f"Brief : {top_articles[0]['description']}.")
        send_sms(message_content)


def get_news():
    global top_articles
    response = requests.get(NEWS_API_ENDPOINT, NEWS_API_PARAMS)
    response.raise_for_status()
    data = response.json()
    top_articles = data['articles']


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


check_stock_movement()
