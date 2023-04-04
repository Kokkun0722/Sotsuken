# https://qiita.com/hitomatagi/items/f9d4d6b816d729132231

import cv2
import numpy as np
import time
import datetime
import requests
import Main_ChatBot_System as MCS
import Call_Out

# 定数定義
FRAME_RATE = 30  # fps
THROUD=2.5*(10**6)

# 設定値
EXIST_LIMIT_T=2
EXIST_LIMIT_F=2

# 検知結果
prev_exist=False
human_exist=False
human_move=0
exist_sum_T=0
exist_sum_F=0

shot_flag=False
prev_exist_flag=[0,0]

isStarted=False

# 画像送信の定数
url = "https://notify-api.line.me/api/notify" 
token = "XfeZrJIh1meAmMM38vJVlDoKvfzY2HrX2PpPEFqWRir"
headers = {"Authorization" : "Bearer "+ token} 
            
def Motion_Detection(frame):
    # 入力画像を浮動小数点型に変換
    frame = frame.astype(np.float32)
    
    # 差分計算
    diff_frame = cv2.absdiff(frame, back_frame)

    # 背景の更新
    cv2.accumulateWeighted(frame, back_frame, 0.025)
    
    # matをnp.arrayに変換
    diff=diff_frame.astype(np.uint8)
    
    # gray_diffを作る
    gray_diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    
    # 色を付ける
    bright=np.sum(gray_diff)
    if(bright>THROUD):
        color=(0,0,255)
    else:
        color=(255,255,0)
    gray_diff=cv2.cvtColor(gray_diff,cv2.COLOR_GRAY2BGR)
    cv2.rectangle(gray_diff, (50, 80), (125, 130), color, thickness=-1)
    
    #フラグと画像を返す
    return (bright>THROUD,gray_diff)

def LINE_UpLoder(frame):
    print("書き記す！！！")
    cv2.imwrite("output.jpg", frame)
    time.sleep(2)

    dt_now = datetime.datetime.now()
    payload = {"message" :  "\n"+str(dt_now)+"\n"}
    image = r'C:\Users\kokku\output.jpg'
    files = {'imageFile': open(image, 'rb')}

    print("送信！")
    res = requests.post(url,params=payload,headers=headers,files=files)

Call_Out.Call("カメラから離れて、起動までお待ちください。")

# 元ビデオファイル読み込み
cap = cv2.VideoCapture(0)

# 最初のフレーム読み込み
ret, frame = cap.read()

# 背景フレーム
back_frame = np.zeros_like(frame, np.float32)

# 変換処理ループ
while ret == True:
    
    # 動体検知を行う    
    flag,diff=Motion_Detection(frame)
    
    if(not isStarted and not flag):
            Call_Out.Call("起動しました！！！")
            isStarted=True
            
            
    cv2.imshow("diff",diff)
    
    # フラグを作る
    human_exist=flag
    human_move=int(human_exist)-int(prev_exist)
    
    # 存在の合計をとる
    if(human_exist):
        exist_sum_F=0
        exist_sum_T=exist_sum_T+1
    else:
        exist_sum_T=0
        exist_sum_F=exist_sum_F+1
    
    exist_flag=[exist_sum_T>EXIST_LIMIT_T*FRAME_RATE,exist_sum_F>EXIST_LIMIT_F*FRAME_RATE]
    exist_diff=[exist_flag[0]-prev_exist_flag[0],exist_flag[1]-prev_exist_flag[1]]
    
    # カメラフラグ関連
    if(exist_diff[0]==1 and not shot_flag):
        if(isStarted):
            LINE_UpLoder(frame)
            MCS.Main()
            shot_flag=True
    if(exist_diff[1]==-1):
        shot_flag=False
    
    print(exist_flag,exist_diff,shot_flag)
    
    print()
    
    # 'q'キーが押された場合は終了する
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # 待機
    time.sleep(1/FRAME_RATE)
    
    # 現在のフレームを前フレームとして更新する
    prev_exist=human_exist
    prev_exist_flag=exist_flag
    
    # 次のフレーム読み込み
    ret, frame = cap.read()

# 終了処理
cv2.destroyAllWindows()
cap.release()