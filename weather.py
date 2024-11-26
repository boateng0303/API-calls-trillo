import urllib.request
import json

def get_weather(city='toronto', api_key=''):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    weather = result['weather'][0]['description']
    temperature = round(result['main']['temp'] - 273.15, 2)
    return f"The weather in {city} is {weather} with a temperature of {temperature}°C"


