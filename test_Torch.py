import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

import torch
import torchvision
from torchvision import transforms

# 画像の読み込み
image_path=r"C:\Users\kokku\Desktop\声掛けカメラプログラム\man.png"
pil_img=Image.open(image_path)
img=np.array(pil_img)

cv2.imshow("image", img)
cv2.waitKey(2000)