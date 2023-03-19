import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

human_rects = human_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

if len(human_rects) > 0:
    # 人間が見つかった場合
    for (x,y,w,h) in human_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    human_img = frame
else:
    # 人間が見つからなかった場合
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x,y,w,h = cv2.boundingRect(contours[0])
    human_img = frame[y:y+h, x:x+w]

cv2.imshow('human_only', human_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
