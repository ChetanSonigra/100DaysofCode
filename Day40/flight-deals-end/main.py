#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import smtplib,os
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager


datamanager = DataManager()
datamanager.get_max_prices()
flight_data = FlightData()
notification_manager = NotificationManager()

datamanager.add_IATA_code()

while True:
    print("Welcome to Chetan's flight club.")
    print("We find the best flight deals and email you.")
    user_fname = input('What is your first name? ')
    user_lname = input('What is your last name? ')
    user_email = input('What is your email? ')
    user_email_confirmation = input('Type your email again.')
    if user_email == user_email_confirmation:
        datamanager.add_user(user_fname,user_lname,user_email)
        print('You are in the club!')
    else:
        print("Email didn't match. Try again!")
    add_more = input('Do you want to add? (y/n) ').lower()
    if add_more=='n':
        break

datamanager.get_users()

for city in datamanager.destination_data:
    recipient_mails = [user['email'] for user in datamanager.users if 'email' in user]
    cheapest_flight = flight_data.find_cheapest_flight('AMD',city['iataCode'])
    my_price = city['lowestPrice']
    if cheapest_flight['price']<my_price:
        notification_manager.send_mail(notification_manager.my_email,recipient_mails,cheapest_flight,city)







