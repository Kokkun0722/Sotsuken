# https://qiita.com/hitomatagi/items/f9d4d6b816d729132231

import cv2
import numpy as np
import math

# 定数定義
ESC_KEY = 27     # Escキー
INTERVAL= 33     # インターバル
FRAME_RATE = 30  # fps
THROUD=2.5*(10**6)

# 元ビデオファイル読み込み
mov_org = cv2.VideoCapture(0)

# 最初のフレーム読み込み
has_next, i_frame = mov_org.read()

# 背景フレーム
back_frame = np.zeros_like(i_frame, np.float32)

# 変換処理ループ
while has_next == True:
    # 入力画像を浮動小数点型に変換
    f_frame = i_frame.astype(np.float32)

    # 差分計算
    diff_frame = cv2.absdiff(f_frame, back_frame)

    # 背景の更新
    cv2.accumulateWeighted(f_frame, back_frame, 0.025)
    
    # matをnp.arrayに変換
    back=back_frame.astype(np.uint8)
    diff=diff_frame.astype(np.uint8)
    
    # gray_diffを作る
    gray_diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    
    # 色を付ける
    bright=np.sum(gray_diff)
    if(bright<THROUD):
        color=(255,255,0)
    else:
        color=(0,0,255)
    
    gray_diff=cv2.cvtColor(gray_diff,cv2.COLOR_GRAY2BGR)
    cv2.rectangle(gray_diff, (50, 80), (125, 130), color, thickness=-1)
    
    # フレーム表示
    cv2.imshow("gray",gray_diff)
    
    # Escキーで終了
    key = cv2.waitKey(INTERVAL)
    if key == ESC_KEY:
        break

    # 次のフレーム読み込み
    has_next, i_frame = mov_org.read()

# 終了処理
cv2.destroyAllWindows()
mov_org.release()