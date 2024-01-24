import requests
from datetime import datetime
import os
query = input("Tell me which exercise you did:")
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
GENDER = "Male"
WEIGHT_KG = "71"
HEIGHT_CM = "178"
AGE = "22"

link = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
paramaters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=link, headers=header, json=paramaters)
# print(response.json["exercises"][0]["duration"])
dictionary = response.json()
print()

today = datetime.now()
date = today.strftime('%d/%m/%Y')
time = today.strftime("%T")
sheety_ulr = "https://api.sheety.co/58e36deebcd1bc3094d6c9bb62a05a92/workoutes/workouts"
sheety_header ={
    "Authorization": "Basic a2FuZWRneTp0ZXN0dGVzdA==",
}
sheety_param = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": dictionary["exercises"][0]["name"].title(),
      "duration": dictionary["exercises"][0]["duration_min"],
      "calories": dictionary["exercises"][0]["nf_calories"],
      "id": 2,
        }
}

result = requests.post(url=sheety_ulr, json=sheety_param, headers= sheety_header)
print(result.text)
