# このプログラムは、
# Webカメラを使って監視カメラのようなものを作り、
# 人が部屋に入ったり出たりした場合に、
# その瞬間の画像と入室/退室のタイムスタンプを
# LINE Notifyを使って送信するプログラムです。

import cv2
import time
import requests
import datetime

import Call_Out

# 設定値
HUMAN_THRESHOLD=500
FRAME_RATE=5
EXIST_LIMIT_T=2
EXIST_LIMIT_F=5

# 検知結果
prev_exist=False
human_exist=False
human_move=0

exist_sum_T=0
exist_sum_F=0

# その他変数
shot_flag=False

# 画像送信の定数
url = "https://notify-api.line.me/api/notify" 
token = "XfeZrJIh1meAmMM38vJVlDoKvfzY2HrX2PpPEFqWRir"
headers = {"Authorization" : "Bearer "+ token} 

# カメラのキャプチャを開始する
cap = cv2.VideoCapture(0)

# 前フレームの画像
prev_frame = None
prev_exist_flag=[0,0]

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

    # 閾値を設定して、差分画像を2値化する
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    # 輪郭を抽出する
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 面積の総和
    count = 0

    # 輪郭があれば、変化があったことを示す赤い矩形を描画する
    rect_num = 0
    center_sum_x = 0
    center_sum_y = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rect_num += 1
        count += w * h
        if(human_exist):
            color=(0, 0, 255)
        else:
            color=(255,255,0)
        cv2.rectangle(diff, (x, y), (x+w, y+h), color, 2)

    # 変化が大きければOを、そうでなければXを表示
    centroid=None
    if(count>HUMAN_THRESHOLD):
        human_exist=True
    else:
        human_exist=False
                
    # 結果を表示する
    human_move=human_exist-prev_exist
    # print(human_exist,human_move)        
    cv2.imshow('frame', diff)
    
    #別の処理を行う
    # 存在の合計をとる
    if(human_exist):
        exist_sum_F=0
        exist_sum_T=exist_sum_T+1
    else:
        exist_sum_T=0
        exist_sum_F=exist_sum_F+1
        
    exist_flag=[exist_sum_T>EXIST_LIMIT_T*FRAME_RATE,exist_sum_F>EXIST_LIMIT_F*FRAME_RATE]
    exist_diff=[exist_flag[0]-prev_exist_flag[0],exist_flag[1]-prev_exist_flag[1]]
    
    print(exist_diff)
    
    #完全に人がいる/いないを判定
    # if(exist_diff[0]):
    #     dt_now = datetime.datetime.now()
    #     print(dt_now,"〇",exist_diff[0])
    # elif(exist_diff[1]):
    #     dt_now = datetime.datetime.now()
    #     print(dt_now,"✕",exist_diff[1])
        
    if(exist_diff[0]==1 and not shot_flag):
        #写真を送る
        Call_Out.Call()   
        print("書き記す！！！")
        cv2.imwrite("output.jpg", frame)
        time.sleep(2)
    
        dt_now = datetime.datetime.now()
        payload = {"message" :  "\n"+str(dt_now)+"\n"}
        image = r'C:\Users\kokku\output.jpg'
        files = {'imageFile': open(image, 'rb')}
    
        print("送信！")
        shot_flag=True
        res = requests.post(url,params=payload,headers=headers,files=files)
    
    if(exist_diff[1]==-1):
        shot_flag=False
    
    # 現在のフレームを前フレームとして更新する
    prev_frame = gray
    prev_exist=human_exist
    prev_exist_flag=exist_flag

    # キー入力を待つ
    key = cv2.waitKey(1) & 0xFF

    # 'q'キーが押された場合は終了する
    if key == ord('q'):
        break
    
    # 少し待つ
    time.sleep(1/FRAME_RATE)

# キャプチャをリリースし、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()