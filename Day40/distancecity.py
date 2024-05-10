import requests,os

url = "https://distanceto.p.rapidapi.com/distance/route"

payload = { "route": [
		{
			"country": "IN",
			"name": "Rajkot"
		},
		{
			"country": "IN",
			"name": "Ahmedabad"
		}
	] }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
	"X-RapidAPI-Host": "distanceto.p.rapidapi.com",
    "car": 'True'
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())