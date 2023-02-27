# https://blog.memo-labo.com/?p=1739

import requests
import datetime,pytz

url = "https://notify-api.line.me/api/notify" 
token = "EZ5RahD4S0WXj4B8MgaDSJJ6GjLDGVljteB807FdjFY"
headers = {"Authorization" : "Bearer "+ token} 
message =  datetime.datetime.now(pytz.timezone('Asia/Tokyo')) 
payload = {"message" :  "\n"+str(message)}
image = r'C:\Users\kokku\output.jpg'
files = {'imageFile': open(image, 'rb')}
res = requests.post(url,params=payload,headers=headers,files=files)