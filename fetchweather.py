import requests
from datetime import datetime
import json

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
api_key="dbc3a3e175mshca7c65f82c770a0p19233bjsnc61fa50c82d1"
api_host="community-open-weather-map.p.rapidapi.com"
querystring = {"q":"Los Angeles"}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": api_host
}

response = requests.request("GET", url, headers=headers, params=querystring)

weatherdata = response.json

with open('weather.json', 'w', encoding='utf-8') as f:
    json.dump(weatherdata, f, ensure_ascii=False, indent=4)
    
