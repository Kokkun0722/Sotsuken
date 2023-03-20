import cv2
import rembg
import numpy as np
import time
from rembg import remove
from PIL import Image

cap = cv2.VideoCapture(0)

while True:
    start=time.time()
    
    # カメラからフレームをキャプチャ
    ret, frame = cap.read()
    # frame=cv2.resize(frame,(80,80))
    
    # PIL Imageに変換
    input_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 背景を除去
    output_image = remove(input_image)

    # OpenCV画像に変換
    output_image = cv2.cvtColor(np.array(output_image), cv2.COLOR_RGB2BGR)

    # 画像を表示
    cv2.imshow("output", output_image)

    # キー入力を待ち、'q'が押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    print(time.time()-start)
    time.sleep(5)

# 後始末
cap.release()
cv2.destroyAllWindows()
