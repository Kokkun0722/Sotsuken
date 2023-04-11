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
        message = "今日は雨が降っています。出かけるのであれば、傘を忘れずに。"
    elif weather == 'Snow':
        message = "今日は雪が降っています。雪で滑ると危ないので、家で待機しましょう。"
    elif temperature < 10:
        message = "今日は寒いですね。上着などを羽織った方がいいですよ。"
    elif temperature > 30:
        message = "今日は暑いですね。スポーツドリンクを持っておきましょう。"
    else:
        message = "どこかへ出かけるのですか？気を付けてくださいね。"
    return (greeting,message)