# camelcamelcamel to see past price history for any product.

# get your browser headers by going through below linke
# https://myhttpheader.com/
import requests,lxml,smtplib,os
from bs4 import BeautifulSoup
from browser_headers import headers, MY_EMAIL

amzn_link = "https://www.amazon.in/dp/B0BY8JZ22K?FORM=SSAPC1&th=1"
target_price = 21000
amzn_item = "OnePlus Nord CE 3 Lite 5G (Pastel Lime, 8GB RAM, 128GB Storage)"

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com",port=587) as con:
        con.starttls()
        con.login(user=MY_EMAIL,password=os.environ.get("MY_EMAIL_PASSWD"))
        con.sendmail(from_addr=MY_EMAIL,
                     to_addrs=MY_EMAIL,
                     msg=f"Subject: Amazon Price Alert!\n\n{message}")

response = requests.get(amzn_link,headers=headers)

amzn_page = response.text

amzn_soup = BeautifulSoup(amzn_page,"lxml")

price = amzn_soup.find(name="span",class_="a-price-whole")

current_price = float(price.getText().replace(",",""))
# print(current_price)

if current_price<target_price:
    message = f"Hi there,\n Your item {amzn_item} is now available for Rs. {current_price}.\n Checkout at {amzn_link}"
    send_mail(message)