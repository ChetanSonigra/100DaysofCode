import requests,datetime,os

USERNAME = 'chetan44'
TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPH_ID = 'graph1'
today=datetime.datetime(year=2024,month=5,day=6)
DAY = today.strftime('%Y%m%d')

pixela_endpoint = 'https://pixe.la/v1/users'

usr_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_endpoint,json=usr_params)
# print(response.text)
# https://pixe.la/@chetan44

graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN':TOKEN	
}

# response = requests.post(graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
# https://pixe.la/v1/users/chetan44/graphs/graph1.html

pixel_creation_endpoint =  f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.datetime(year=2024,month=5,day=6)
# Use of strftime to get data in specific string format

pixel_params = {
    'date': today.strftime('%Y%m%d'), 
    'quantity': '15'
}

# response = requests.post(pixel_creation_endpoint,json=value_params,headers=headers)
# print(response.text)
# https://pixe.la/v1/users/chetan44/graphs/graph1.html


pixel_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DAY}'

update_pixel_params = {
    'quantity': '10'
}

# response = requests.put(pixel_update_endpoint,json=update_pixel_params,headers=headers)
# print(response.text)
# https://pixe.la/v1/users/chetan44/graphs/graph1.html


pixel_delete_endpoint = pixel_update_endpoint

# response = requests.delete(pixel_delete_endpoint,headers=headers)
# print(response.text)