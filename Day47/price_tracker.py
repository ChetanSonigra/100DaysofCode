# camelcamelcamel to see past price history for any product.

# get your browser headers by going through below linke
# https://myhttpheader.com/
import requests,lxml,smtplib,os
from bs4 import BeautifulSoup
# from browser_headers import headers, MY_EMAIL

MY_EMAIL = os.getenv("MY_EMAIL")
RECIPIENT_MAIL = os.getenv("RECIPIENT_MAIL")
amzn_link = os.getenv("AMZN_LINK")
target_price = float(os.getenv("TARGET_PRICE"))
amzn_item = os.getenv("AMZN_ITEM")

def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com",port=587) as con:
        con.starttls()
        con.login(user=MY_EMAIL,password=os.getenv("MY_EMAIL_PASSWD"))
        con.sendmail(from_addr=MY_EMAIL,
                     to_addrs=RECIPIENT_MAIL,
                     msg=f"Subject: Amazon Price Alert!\n\n{message}")

response = requests.get(amzn_link) #headers=headers

amzn_page = response.text

amzn_soup = BeautifulSoup(amzn_page,"lxml")

price = amzn_soup.find(name="span",class_="a-price-whole")

current_price = float(price.getText().replace(",",""))
# print(current_price)

if current_price<target_price:
    message = f"Hi there,\n Your item {amzn_item} is now available for Rs. {current_price}.\n Checkout at {amzn_link}"
    send_mail(message)