# https://overs.zigexn.co.jp/technology/advent_calendar/7267/

import requests, json,io
from pydub import AudioSegment
from pydub.playback import play

host = "127.0.0.1"
port = 50021

params = (
    ("text", "田中さんこんにちは、今日も良い天気ですね。"),
    ("speaker", 50)
)

response1 = requests.post(
    f"http://{host}:{port}/audio_query",
    params=params
)

response2 = requests.post(
    f"http://{host}:{port}/synthesis",
    headers={"Content-Type": "application/json"},
    params=params,
    data=json.dumps(response1.json())
)

audio_data = response2.content
audio_segment = AudioSegment.from_wav(io.BytesIO(audio_data))
play(audio_segment)
