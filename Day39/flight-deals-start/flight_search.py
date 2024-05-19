import requests,os
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.rapid_api_airports_endpoint = "https://airports15.p.rapidapi.com/airports"
        self.headers = {
            "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
            "X-RapidAPI-Host": "airports15.p.rapidapi.com"
        }              
    
    def get_IATA_code(self,city: str):
        querystring = {"name":city,"page":"1","page_size":"20","sorted_by":"icao"}
        response = requests.get(self.rapid_api_airports_endpoint, headers=self.headers, params=querystring)
        data = response.json()
        # print(data)
        return data['data'][0]['iata_code']
    
