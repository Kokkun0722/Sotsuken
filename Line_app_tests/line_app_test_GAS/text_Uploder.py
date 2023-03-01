# 文字列を入力すると、LINEにアップされる

import json
import requests

url = "https://script.google.com/macros/s/AKfycbwKUmsObuGZPhrUMj47DAe9EEcbgKLrg0BCS67vwUfP82WNHWlC5YLWE-faT5Ky9plYCg/exec"

input_text=input(">")

# JSON形式でデータを用意してdataに格納
data = {
	"text": input_text,
}
# json.dumpでデータをJSON形式として扱う
r = requests.post(url, data=json.dumps(data))
print(r)