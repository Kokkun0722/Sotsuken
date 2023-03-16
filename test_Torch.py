import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

import torch
import torchvision
from torchvision import transforms

# カメラのキャプチャを開始する
cap = cv2.VideoCapture(0)

# 前フレームの画像
prev_frame = None

def Diff_to_Thresh(diff):
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    return thresh

while True:

    # カメラからフレームを取得する
    ret, frame = cap.read()

    # キャプチャに失敗した場合は終了する
    if not ret:
        break

    # グレースケールに変換する
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 初めてのフレームの場合は前フレームを更新する
    if prev_frame is None:
        prev_frame = gray
        continue
    
    # 2つのフレームの差分を求める
    diff = cv2.absdiff(prev_frame, gray)

    # 輪郭を抽出する
    thresh=Diff_to_Thresh(diff)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    # 結果を表示する
    cv2.imshow('frame', frame)

    # 現在のフレームを前フレームとして更新する
    prev_frame = gray

    # キー入力を待つ
    key = cv2.waitKey(1) & 0xFF

    # 'q'キーが押された場合は終了する
    if key == ord('q'):
        break
    
# キャプチャをリリースし、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()