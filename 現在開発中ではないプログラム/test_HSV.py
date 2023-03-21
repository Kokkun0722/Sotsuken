import cv2
import numpy as np
import time

def HSV_Devider(frame):
    # HSVに分解する
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(img)
    return (h,s,v)

# cap = cv2.VideoCapture(0)

# while True:
#     # カメラからフレームをキャプチャ
#     ret, frame = cap.read()
#     h,s,v=HSV_Devider(frame)    
    
#     # 画像を表示
#     cv2.imshow('h', h)
#     cv2.imshow('s', s)
#     cv2.imshow('v', v)

#     # キー入力を待ち、'q'が押されたら終了
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
#     time.sleep(1/60)
    
# # 後始末
# cap.release()
# cv2.destroyAllWindows()