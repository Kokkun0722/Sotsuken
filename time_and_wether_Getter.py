import datetime
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Osaka,jp&appid=6ede9ed22792cac255e34716b8631074&lang=ja&units=metric"

def GetTime():
    now = datetime.datetime.now()
    if 0 <= now.hour < 6:
        greeting = ("深夜","こんばんは。")
    elif 6 <= now.hour < 12:
        greeting = ("朝","おはようございます。")
    elif 12 <= now.hour < 18:
        greeting = ("昼","こんにちは。")
    else:
        greeting = ("夜","こんばんは。")
    return (now,greeting)

def GetWeather():
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = int(data["main"]["temp"])
    return (weather,temperature)