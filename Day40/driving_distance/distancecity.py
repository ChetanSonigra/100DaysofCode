import requests,os
import pandas as pd

url = "https://distanceto.p.rapidapi.com/distance/route"

open_route_service_token = os.environ.get('RAPID_API_KEY')

cities = ['Madurai','Hubli','Pondicherry','Tirupur','Bangarapet','Kottayam',
          'Manipal','Shimoga','Erode','Nellore','Perumbavoor','Salem']

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": open_route_service_token,
	"X-RapidAPI-Host": "distanceto.p.rapidapi.com",
    "car": 'True'
}

n = len(cities)

for i in range(n):
    for  j in range(i+1,n):
        payload = { "route": [
				{
					"country": "IN",
					"name": cities[i]
				},
				{
					"country": "IN",
					"name": cities[j]
				}
			] }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        response.raise_for_status()
        print(data['route']['car']['distance'])
        print(f"{payload['route'][0]['name']}, {payload['route'][1]['name']} {data['route']['car']['distance']}\n")
        with open('100DaysofCode/Day40/driving_distances.csv','a') as f:
            f.write(f"{payload['route'][0]['name']}, {payload['route'][1]['name']}, {data['route']['car']['distance']}\n")
