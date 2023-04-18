import cv2
import numpy as np
import time
import datetime
import requests

# 初期設定

FPS = 60
THROUD = 2.5e6

EXIST_LIMIT_T = 1
EXIST_LIMIT_F = 2

prev_exist = False
human_exist = False
human_move = 0
exist_sum_T = 0
exist_sum_F = 0

shot_flag = False
prev_exist_flag = [0, 0]

isStarted = False

url = "https://notify-api.line.me/api/notify"
token = "XfeZrJIh1meAmMM38vJVlDoKvfzY2HrX2PpPEFqWRir"
headers = {"Authorization": "Bearer " + token}

exist_sum_T=0
exist_sum_F=0
prev_exist_flag=[0,0]

# 関数定義

def Motion_Detection(frame):
    global back_frame
    frame = frame.astype(np.float32)
    diff_frame = cv2.absdiff(frame, back_frame)
    cv2.accumulateWeighted(frame, back_frame, 0.025)
    diff = diff_frame.astype(np.uint8)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    bright = np.sum(gray_diff)
    color = (0, 0, 255) if bright > THROUD else (255, 255, 0)
    gray_diff = cv2.cvtColor(gray_diff, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(gray_diff, (50, 80), (125, 130), color, thickness=-1)

    return bright > THROUD, gray_diff


def LINE_UpLoder(frame):
    cv2.imwrite("output.jpg", frame)
    time.sleep(2)

    dt_now = datetime.datetime.now()
    payload = {"message": "\n" + str(dt_now) + "\n"}
    image = r'C:\Users\kokku\output.jpg'
    files = {'imageFile': open(image, 'rb')}

    requests.post(url, params=payload, headers=headers, files=files)

# カメラを起動・フレーム取得

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
back_frame = np.zeros_like(frame, np.float32)

while ret == True:
    # モーション関数
    flag,diff=Motion_Detection(frame)
    
    # 差分フレームを表示
    cv2.imshow("diff",diff)
    
    # 人が存在していない状態から初めて人が存在したか？
    if(not isStarted and not flag):
        # isStartフラグをTrueに
        isStarted=True
    
    # 人の存在状況を更新し、前回との差分を取る
    human_exist=flag
    human_move=int(human_exist)-int(prev_exist)
    
    # 人が存在する場合、存在時間の制限値を増やす。
    if(human_exist):
        exist_sum_F=0
        exist_sum_T+=1
    # 存在しない場合、非存在時間の制限値を増やす
    else:
        exist_sum_T=0
        exist_sum_F+=1
    
    # 存在時間の制限値に基づいて、存在フラグを判断する
    exist_flag=[exist_sum_T>EXIST_LIMIT_T*FPS,exist_sum_F>EXIST_LIMIT_F*FPS]
    
    # 存在フラグが変化し、かつshot_flagがFalseである場合、LINE通知関数を呼び出す。
    # shot_flagをTrueにする
    if exist_flag[0]-prev_exist_flag[0]==1 and not shot_flag and isStarted:
        LINE_UpLoder(frame)
        shot_flag=True
    # 撮影フラグを偽にする
    elif exist_flag[1]-prev_exist_flag[1]==-1:
        shot_flag=False
        
    # "q"キーが押された？
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    time.sleep(1/FPS)
    
    prev_exist=human_exist
    prev_exist_flag=exist_flag
    
    ret, frame = cap.read()

cv2.destroyAllWindows()
cap.release()