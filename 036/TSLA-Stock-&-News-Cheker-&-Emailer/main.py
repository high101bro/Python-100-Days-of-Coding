
import requests
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GMAIL_ACCOUNT = os.getenv("GMAIL_ACCOUNT")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

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

if diff_percent > 0.1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(
        url=NEWS_ENDPOINT,
        params=news_params,
    )
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    print(articles)
    # [new_item for item in items]

    formatted_articles = [f"""
Headline: {article['title']}.
Published: {article['publishedAt']}
Brief: {article['description']}
Link: {article['url']}
""" for article in articles]

    # recipients = ["daniel.komnick@gmail.com", "lisa.komnick@gmail.com"]
    recipients = ["daniel.komnick@gmail.com"]

    msg = MIMEText("\n".join(formatted_articles))
    msg["Subject"] = f"{COMPANY_NAME} [{STOCK_NAME}] News"
    msg["To"] = ", ".join(recipients)
    msg["From"] = GMAIL_ACCOUNT

    smtp_server = smtplib.SMTP_SSL(
        host='smtp.gmail.com',
        # smtp.gmail.com
        # smtp.live.com
        # smtp.mail.yahoo.com
        port=465
    )

    smtp_server.login(
        user=GMAIL_ACCOUNT,
        password=GMAIL_APP_PASSWORD
    )

    print(f"Sending email to: {recipients}")
    smtp_server.sendmail(
        msg["From"],
        recipients,
        msg.as_string()
    )

    smtp_server.quit()
