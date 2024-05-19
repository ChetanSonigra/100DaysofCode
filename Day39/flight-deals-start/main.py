#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import smtplib,os
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager


datamanager = DataManager()
data_max_prices = datamanager.get_max_prices()
flight_data = FlightData()
notification_manager = NotificationManager()

datamanager.add_IATA_code()

print(data_max_prices)

for city in data_max_prices:
    cheapest_flight = flight_data.find_cheapest_flight('AMD',city['iataCode'])
    my_price = city['lowestPrice']
    if cheapest_flight['price']<my_price:
        notification_manager.send_mail(notification_manager.my_email,cheapest_flight,city)







