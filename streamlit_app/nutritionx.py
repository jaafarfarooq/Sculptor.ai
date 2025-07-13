import requests as re
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
url = os.getenv("url")
def get_nutrition(food):
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': APP_KEY
    }
    data = {
        "query": food
    }

    response = re.post(url, headers=headers, json=data)

    # Print the response
    if response.status_code == 200:
        print("Success:")
        temp = response.json()
        final = dict(list(temp['foods'][0].items())[:15])
        return final
    else:
        return ("Error:", response.status_code, response.text)
    
#print(get_nutrition("1 cup red beans"))