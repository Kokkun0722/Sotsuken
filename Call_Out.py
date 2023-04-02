import pyttsx3
import pygame


#変数
DIR_PATH="C:\\Users\\kokku\Desktop\\声掛けカメラプログラム\\"

def INIT():
    # 初期化
    pygame.init()

def Call(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def Ring(file_name):
    file_path=DIR_PATH+file_name
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def End():
    pygame.mixer.quit()
    
Call("こんにちは")