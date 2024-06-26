import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_endpoint = 'https://api.sheety.co/a44c0ac0ab62df59146a3d3612927846/flightPrices/prices'
        self.headers = {
        'Content-Type': 'application/json'
        }
        self.destination_data = []
         
    def get_max_prices(self):
        resp = requests.get(self.sheety_endpoint)
        data = resp.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def add_IATA_code(self):
        flight_search=FlightSearch()
        print(self.destination_data)
        for city in self.destination_data:
            if not city['iataCode']:
                IATA_CODE = flight_search.get_IATA_code(city['city'])
                body = {
                    'price': {
                        'iataCode': IATA_CODE
                    }
                }
                resp = requests.put(f"{self.sheety_endpoint}/{id}",json=body,headers=self.headers)
                print(resp.text)




