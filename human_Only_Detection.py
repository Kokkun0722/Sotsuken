import cv2
import numpy as np

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0)

def GrayScale(img):
    # グレースケール
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # エッジ認識
    edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)
    
    # 輪郭を見つける
    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]
    
    # 一番大きい輪郭を使ってマスクを作る
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))
    
    # マスクをスムージングさせ、3チャネルにする
    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
    mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

    return mask_stack

# 動体検知のための背景差分法のインスタンスを作成する
fgbg = cv2.createBackgroundSubtractorMOG2()

# カメラからの入力を取得する
cap = cv2.VideoCapture(0)

while True:
    # フレームを読み込む
    ret, frame = cap.read()

    # 背景差分法を適用する
    gray=GrayScale(frame)

    # 結果を表示する
    # cv2.imshow('frame', frame)
    cv2.imshow('fgmask', gray)

    # キー入力を待つ
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
cap.release()
cv2.destroyAllWindows()