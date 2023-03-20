import rembg

from rembg import remove
from PIL import Image

path_str="C:\\Users\\kokku\\Desktop\\声掛けカメラプログラム\\"

input_path=path_str+"man.jpg"
output_path=path_str+"out.png"

input_image=Image.open(input_path)
output_image=remove(input_image)
output_image.save(output_path)