import requests,datetime,smtplib,time

MY_LAT = 22.303894   # got it from latlong.net
MY_LONG = 70.802162
MY_EMAIL = 'abc@gmail.com'
MY_PASSWORD = 'abc@1234'

my_position = (MY_LONG,MY_LAT)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
response.raise_for_status()
data = response.json()
# print(data)

longitude = float(data['iss_position']['longitude'])
latitude = float(data['iss_position']['latitude'])

iss_position = (longitude,latitude)

# print(iss_position)

# if response.status_code != 200:
#     raise Exception('Bad response from ISS API')
# elif response.status_code==400:
#     raise Exception('Resource Not Found')
# elif response.status_code==401:
#     raise Exception('You are not authorized to access this data.')


parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzid': 'Asia/Kolkata'
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0]) # getting only hour part
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
# print(sunrise,sunset,sep='\n')


def is_iss_near(my_position,iss_position):
    if my_position[0]-5< iss_position[0] <my_position[0]+5:
        if my_position[1]-5 < iss_position[1] < my_position[1]+5:
            return True
    return False

def is_night():
    now = datetime.datetime.now().hour
    if now>=sunset or now<sunrise:
        return True
    return False

# print(is_iss_near(my_position,iss_position),is_night())
while True: 
    if is_iss_near(my_position,iss_position) and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg='Subject: Look Up\n\nISS is near you. please look in the sky to see.')
    time.sleep(6000)