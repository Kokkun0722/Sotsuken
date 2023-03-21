import pyttsx3
import pygame

#変数
DIR_PATH="C:\\Users\\kokku\Desktop\\声掛けカメラプログラム\\"

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

Call("おっぱお")
Ring("start.mp3")
Ring("finish.mp3")
End()
    
#「今は深夜の12時ですよ？」
#「雨降ってますよ？」

# # 喋らせる言葉　例えば「時間に応じて、こんな時間にお出かけですか？のような声掛けを行ないたい」「家族に通知を入れたい」。
