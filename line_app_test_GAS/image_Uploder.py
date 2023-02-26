import requests
import io
import cv2

url = "https://script.google.com/macros/s/AKfycbxp8nnMsfuacXjlF8HE4RdLA4bxOZOA5Javi-lapjBAIFYtgKHIBkW-NZOHlUcpef-GqQ/exec"

# カメラの設定
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 画像のキャプチャと送信
with io.BytesIO() as stream:
    ret, frame = cap.read()
    cv2.imwrite("image.jpg", frame)
    files = {"file": open("image.jpg", "rb")}
    r = requests.post(url, files=files)
print(r)
