import os

MY_WEATHER_API_KEY =  os.environ.get('OWM_API_KEY')
MY_LAT = 22.303894   # got it from latlong.net
MY_LONG = 70.802162
MY_CITY ='Rajkot,IN'
MY_EMAIL = 'abc@gmail.com'
MY_PASSWORD= 'abc@1234'
account_sid = 'acb'
auth_token = 'dfs'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'cnt': 7,
    'appid': MY_WEATHER_API_KEY
}

import requests,smtplib
from twilio.rest import Client

response = requests.get(url='https://api.openweathermap.org/data/2.5/weather',params=parameters)
response.raise_for_status()
print(response.json())

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
# print(response.json())
data = response.json()['list']

will_rain = False
for x in data[2:]:
    if x['weather'][0]['id']<700:
        # print('Bring an umbrell')
        will_rain = True
        # print(x['dt_txt'])


# Use twillio to use api for sending sms, making calls/watsapp msg and much more.
if will_rain:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject: Rain is coming\n\nRemember to bring an umbrella, It's going to rain today.")
    
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
            body ="It's going to rain today. Remember to bring an umbrella.",
            from_ = "+1254544",     # number generated from twilio
            to = "+342463"         # your verified number
        )
    print(message.status)

# max_temp = 0
# for x in data:
#     if x['main']['temp']>max_temp:
#         max_temp = x['main']['temp']
#     if x['weather'][0]['main'] != 'Clear':
#         print(x)
    
# print(max_temp)


# Environment variables: 
# Why? 1. convenience(No need to change code frequently,just change the env variables.) 
# 2. security 
# create env variable in os and use os.environ.get("var_name")
# another way is to use dotenv module.

# Explore apilist.fun