import requests as re
'''import json

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}
data = {
    "query": "grape"
}

response = re.post(url, headers=headers, json=data)

# Print the response
if response.status_code == 200:
    print("Success:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)'''

API_URL = "http://localhost:8000/TDEE/"  # Change this to your actual FastAPI URL
payload = {
    "weight_kg": 100,
    "height_cm": 200,
    "age": 20,
    "gender": "male",
    "activity_level": "sedentary",
    "goal": "cut"
}

response = re.post(API_URL, json=payload)
print(response.json())