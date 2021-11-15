import requests
import json
import config


url = f"https://api.openweathermap.org/data/2.5/weather?appid={config.token}&q=Moscow"
req = requests.get(url).json()

with open('openweathermap_response.json', 'w') as f:
    json.dump(req, f)



