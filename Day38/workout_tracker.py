
import requests,datetime,os

nutritionix_key = os.environ.get('NUTRITIONIX_API_KEY')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
app_id = 'a40caabd'
GENDER = 'MALE'
WEIGHT_KG = 68
HEIGHT_CM = 177.8
AGE = 26


host_domain = 'https://trackapi.nutritionix.com'

exercise_endpoint = '/v2/natural/exercise'

user_input = input('Tell me which exercise you did? ')

headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id,
    'x-app-key': nutritionix_key
}

exercise_params = {
    'query': user_input,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(f'{host_domain}{exercise_endpoint}',json=exercise_params,headers=headers)
exercises = response.json()
print(exercises,type(exercises))
sheety_endpoint= 'https://api.sheety.co/a44c0ac0ab62df59146a3d3612927846/workoutTracking/workouts'

now = datetime.datetime.now()


for exercise in exercises['exercises']:
    sheety_params = {
        'workout': {
            'date': now.strftime('%d/%m/%Y'),
            'time': now.strftime('%H:%M:%S'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': SHEETY_TOKEN
    }
    response=requests.post(sheety_endpoint,json=sheety_params,headers=headers)
    print(response.text)
    

# Get: 
# response = requests.get(sheety_endpoint)   
# workouts = response.json()
# print(workouts,type(workouts))


# Delete: 
# for workout in workouts['workouts']:
#     response = requests.delete(f"{sheety_endpoint}/2")
#     print(response.text)