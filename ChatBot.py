import datetime
import requests

def ChatBot():

    # 現在の時間を取得
    now = datetime.datetime.now()
    hour = now.hour

    # 天気情報を取得
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Osaka,jp&appid=6ede9ed22792cac255e34716b8631074&lang=ja&units=metric")
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    weather = weather_data['weather'][0]['main']

    # 家にとどまるように促すメッセージを定義
    stay_home_message = "今日は外出せずに家でお過ごしになることをおすすめします。"

    # 現在の時間に応じたメッセージを選択
    if 5 <= hour < 12:
        greeting = "おはようございます。"
    elif 12 <= hour < 18:
        greeting = "こんにちは。"
    else:
        greeting = "こんばんは。"

    # 天気や温度に応じたメッセージを追加
    if 19 <= hour <= 23:
        message="外はもう暗いですね。今日はもう外出せずに、寝ることをお勧めします。"
    elif 0 <= hour <= 6:
        message="もう夜も遅いので、危ないですよ。眠れないのであれば、寝室でリラックスするといいかもしれませんよ。"
    elif weather == 'Rain':
        message = "今日は雨が降っています。今日は外出せずに、家でお過ごしになることをおすすめします。"
    elif weather == 'Snow':
        message = "今日は雪が降っています。今日は外出せずに、家でお過ごしになることをおすすめします。"
    elif temperature < 10:
        message = "今日は寒いですね。今日は外出せずに、家でお過ごしになることをおすすめします。"
    elif temperature > 30:
        message = "今日は暑いですね。今日は外出せずに、家でお過ごしになることをおすすめします。"
    else:
        message = stay_home_message
    return (greeting,message)