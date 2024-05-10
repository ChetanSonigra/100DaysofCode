#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager


datamanager = DataManager()
data_max_prices = datamanager.get_max_prices()

datamanager.add_IATA_code()



