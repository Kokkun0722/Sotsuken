# 上記の例では、OpenWeatherMap APIキーを使用する必要があるため、自分自身でAPIキーを取得して変数<YOUR_API_KEY>に代入する必要があります。また、lang=jaをAPIリクエストに含めることで、天気情報が日本語で取得されます。

import datetime
import requests
import Call_Out

# OpenWeatherMap APIのURLとAPIキー
url = "https://api.openweathermap.org/data/2.5/weather?q=Osaka,jp&appid=6ede9ed22792cac255e34716b8631074&lang=ja&units=metric"

# 天気情報を取得
response = requests.get(url)
data = response.json()

# 現在の時刻を取得
now = datetime.datetime.now()

# 時間に応じて挨拶を変更する
if 0 <= now.hour < 6:
    greeting = "深夜"
elif 6 <= now.hour < 12:
    greeting = "朝"
elif 12 <= now.hour < 18:
    greeting = "昼"
else:
    greeting = "夜"

# 天気情報から天候と気温を取得する
weather = data["weather"][0]["description"]
temperature = int(data["main"]["temp"])

# 出力用の文字列を作成する
output = f"現在は、{greeting}の{now.hour}時{now.minute}分、{weather}です。気温は、{temperature}度です。"

# 結果を表示する
print(output)
Call_Out.Call(output)