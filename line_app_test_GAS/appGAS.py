import json
import requests
# import time

url = "https://script.google.com/macros/s/AKfycbw90ao8jiLl89OuPze2atanfCUgoINLAZTseqknrBaBaUCWH22HRYBDod-D_gOONeC8/exec"

# JSON形式でデータを用意してdataに格納
data = {
	"token": "token",
	"mail" : "mail-address",
	"pass" : "password"
}
# json.dumpでデータをJSON形式として扱う
r = requests.post(url, data=json.dumps(data))
print(r)