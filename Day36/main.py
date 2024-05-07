import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY= os.environ.get('ALPHAVANTAGE_KEY')
NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
MY_EMAIL = 'abc@gmail.com'
MY_PASSWORD = 'abc@1234'
account_sid = 'asdf'
auth_token = 'sdfs'


parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_API_KEY
}

import requests,smtplib
from twilio.rest import Client


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url='https://www.alphavantage.co/query',params=parameters)
response.raise_for_status()
# print(response.json())
data = response.json()['Time Series (Daily)']
data = [float(v['4. close']) for v in data.values()]
yesterday_closing = data[0]
day_before_yesterday_closing = data[1]
# print(yesterday_closing,day_before_yesterday_closing)

perc = (yesterday_closing - day_before_yesterday_closing)/day_before_yesterday_closing

if perc<-0.05 or perc>0.05:
    print('Get News')
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_parameters = {
    'q':COMPANY_NAME,
    'from': '2024-04-06',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
    }
    perc=perc*100
    perc= round(perc,2)
    
    if perc>0:
        up_down = '🔺'
    else:
        up_down = '🔻'

    news_response= requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_articles= news_response.json()['articles'][:3]
    # print(news_articles)

    for article in news_articles:
        print(f"Subject: {STOCK}: {up_down}{perc}%\n\nHeadline: {article['title']}\nBrief: {article['description']}\n")


    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        for article in news_articles:
            connection.sendmail(MY_EMAIL,MY_EMAIL,f"Subject: {STOCK}: {up_down}{perc}%\n\nHeadline: {article['title']}\nBrief: {article['description']}\n")
            
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
            body =f"Subject: {STOCK}: {up_down}{perc}%\n\nHeadline: {article['title']}\nBrief: {article['description']}\n",
            from_ = "+1254544",     # number generated from twilio
            to = "+342463"         # your verified number
        )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

