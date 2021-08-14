import requests

def return_weather(city="Phoenix", units="imperial"):
    with open("weatherapikey.txt", "r") as f:
        api_key = f.readline()

    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}")
    weather = weather.json()

    temp = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    condition = weather["weather"][0]["main"]
    
    if units == "imperial":
        return f"The weather for {city}: {condition}. It is {temp} F and feels like {feels_like} F."
    else:
        return f"The weather for {city}: {condition}. It is {temp} C and feels like {feels_like} C." 