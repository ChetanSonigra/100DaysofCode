import datetime,os
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.skyscanner_endpoint = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"
    
    def find_cheapest_flight(self,fromcity,tocity,depart_date=datetime.datetime.today().strftime('%Y-%m-%d')):
        import requests

        querystring = {"fromEntityId":fromcity,"toEntityId":tocity,"departDate":depart_date}

        headers = {
            "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
            "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
        }

        response = requests.get(self.skyscanner_endpoint, headers=headers, params=querystring)
        response.raise_for_status()
        cheapest_flight = response.json()['data'][0]
        # print(cheapest_flight)
        return cheapest_flight
        
        
if __name__=='__main__':
    flight_data = FlightData()
    flight_data.find_cheapest_flight('AMD','BOM')