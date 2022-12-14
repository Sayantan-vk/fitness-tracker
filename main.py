import requests
from datetime import datetime

date = datetime.now()
DATE = date.strftime(f'{"%d"}/{"%m"}/{"%Y"}')
TIME = date.strftime("%X")

MY_ID = "3096e0c9"
MY_API_KEY = "8b44ea183954ecb82a7f027370cbc32d"

GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "170"
AGE = "23"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/0609b7ecb1f1651fdfe57a5e5b661c72/myWorkouts/workouts"

exercise_text = input("**# Tell Me About Your Today's Workouts: ")

headers = {
    "x-app-id": MY_ID,
    "x-app-key": MY_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, )
result = response.json()
data_list=result["exercises"]

for details in data_list:
    user_inputs=details["user_input"].title()
    durations=details["duration_min"]
    calories=details["nf_calories"]

    shetty_data = {"workout": {
        "date":DATE,
        "time":TIME,
        "exercise": user_inputs,
        "duration": f"{durations} min",
        "calories": calories,
         }

    }

    requests_to_shetty= requests.post(url=sheety_url, json=shetty_data)
