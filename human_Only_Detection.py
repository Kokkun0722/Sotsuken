import cv2

# 動体検知のための背景差分法のインスタンスを作成する
fgbg = cv2.createBackgroundSubtractorMOG2()

# カメラからの入力を取得する
cap = cv2.VideoCapture(0)

while True:
    # フレームを読み込む
    ret, frame = cap.read()

    # 背景差分法を適用する
    fgmask = fgbg.apply(frame)

    # ノイズを除去する
    fgmask = cv2.medianBlur(fgmask, 5)

    # 輪郭を検出する
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 各輪郭について、面積が一定以上のものを検知する
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            # 検知した輪郭を矩形で囲む
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 結果を表示する
    cv2.imshow('frame', frame)
    #cv2.imshow('fgmask', fgmask)

    # キー入力を待つ
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
cap.release()
cv2.destroyAllWindows()