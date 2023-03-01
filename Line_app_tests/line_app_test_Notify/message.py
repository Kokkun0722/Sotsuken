import requests
url = "https://notify-api.line.me/api/notify" 
token = "EZ5RahD4S0WXj4B8MgaDSJJ6GjLDGVljteB807FdjFY"
headers = {"Authorization" : "Bearer "+ token} 
message =  "AIUEO!!!" 
payload = {"message" :  message}
image = 'image.jpg'
files = {'imageFile': open(image, 'rb')}
res = requests.post(url,
                    params=payload,
                    headers=headers,
                    files=files)