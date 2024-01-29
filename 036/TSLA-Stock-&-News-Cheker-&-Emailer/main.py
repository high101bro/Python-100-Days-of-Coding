
import requests
from dotenv import load_dotenv
import os

load_dotenv()
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    'apikey': ALPHAVANTAGE_API_KEY,
}
response = requests.get(
    STOCK_ENDPOINT,
    params=parameters
)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# data_list = [new_item for item in list]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_data_closing_price)

difference = abs(yesterday_closing_price - day_before_yesterday_data_closing_price)
print(difference)

diff_percent = (difference / yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 0.05:
    print(NEWS_API_KEY)
    # news_params = {
    #     'apiKey': NEWS_API_KEY,
    #     'qInTitle': COMPANY_NAME,
    # }
    # news_response = requests.get(
    #     url=STOCK_ENDPOINT,
    #     params=news_params,
    # )
    # news_response.raise_for_status()
    # articles = news_response.json() #["articles"]
    # print(articles)

