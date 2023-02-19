# このプログラムは、カメラからの入力を使用して、フレーム間での変化を検出しています。変化が閾値より大きい場合は、赤い長方形と緑色の円を表示して、「O」を出力し、変化が小さい場合は「X」を出力します。フレームレートを設定し、カメラからの入力を待つために時間を少し遅らせています。このプログラムを実行することで、カメラで何かが動いたときにアラートを受け取ることができます。

import cv2
import time

#人間の有無を判別する閾値
HUMAN_THRESHOLD=1000
FRAME_RATE=10

# カメラのキャプチャを開始する
cap = cv2.VideoCapture(0)

# 前フレームの画像
prev_frame = None

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

    # 面積の総和
    count = 0
    
    # 2つのフレームの差分を求める
    diff = cv2.absdiff(prev_frame, gray)

    # 閾値を設定して、差分画像を2値化する
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    # 輪郭を抽出する
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭があれば、変化があったことを示す赤い矩形を描画する
    rect_num = 0
    center_sum_x = 0
    center_sum_y = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rect_num += 1
        count += w * h
        center_x = x + w // 2
        center_y = y + h // 2
        center_sum_x += center_x
        center_sum_y += center_y
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # 変化が大きければOを、そうでなければXを表示
    centroid=None
    if(count>HUMAN_THRESHOLD):
        if rect_num > 0:
            center_x = int(center_sum_x / rect_num)
            center_y = int(center_sum_y / rect_num)
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            centroid=(center_x, center_y)
        print("O")
    else:
        print("X")
        
    # print('長方形の数:', rect_num)
    # print('面積の総和:', count)
    # print('重心座標:', centroid)
    
    # 結果を表示する
    cv2.imshow('frame', frame)
    
    # 現在のフレームを前フレームとして更新する
    prev_frame = gray

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