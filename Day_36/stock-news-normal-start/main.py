import requests
from twilio.rest import Client

# API keys and endpoints
ALPHA_VANTAGE_API_KEY = ''
NEWS_API_KEY = ''
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = '+'
PHONE_NUMBER = ''

# Stock and company details
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# Step 1: Get stock prices
def get_stock_prices():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=params)
    data = response.json()

    # Get yesterday and day before yesterday's closing prices
    time_series = data.get("Time Series (Daily)", {})
    dates = list(time_series.keys())
    yesterday = dates[0]
    day_before_yesterday = dates[1]

    yesterday_close = float(time_series[yesterday]["4. close"])
    day_before_yesterday_close = float(time_series[day_before_yesterday]["4. close"])

    return yesterday_close, day_before_yesterday_close


# Step 2: Get news articles
def get_news():
    params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    data = response.json()

    # Get the first 3 news articles
    articles = data.get("articles", [])[:3]
    return [(article["title"], article["description"]) for article in articles]


# Step 3: Send SMS using Twilio
def send_sms(messages):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for message in messages:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=PHONE_NUMBER
        )


# Main logic to check stock price change and send news if necessary
def check_stock_and_send_news():
    # Get stock prices
    yesterday_close, day_before_yesterday_close = get_stock_prices()

    # Step 3: Calculate the percentage change
    price_diff = abs(yesterday_close - day_before_yesterday_close)
    percentage_diff = (price_diff / day_before_yesterday_close) * 100

    # Step 4: Check if the percentage change is greater than 5%
    if percentage_diff > 5:
        print("Get News")

        # Step 5: Get the news articles
        articles = get_news()

        # Step 6: Format the messages
        messages = []
        change_direction = "🔺" if yesterday_close > day_before_yesterday_close else "🔻"
        percentage_change = round(percentage_diff, 2)

        for title, description in articles:
            message = f"{STOCK_NAME}: {change_direction}{percentage_change}%\nHeadline: {title}\nBrief: {description}"
            messages.append(message)

        # Step 7: Send messages
        send_sms(messages)


if __name__ == "__main__":
    check_stock_and_send_news()
