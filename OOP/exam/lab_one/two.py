import requests, json

complete_url = "https://api.openweathermap.org/data/2.5/weather?q={sylhet}&appid={ba52e5b1274ce7f5a452d58a1edeb59c}"
response = requests.get(complete_url)
date = response.json() 

def weather_date(date):
    print('Date: ', date["main"]["temp"])

weather_date(date)