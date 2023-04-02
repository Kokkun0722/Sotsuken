import speech_recognition as sr
import time

import Call_Out
import ChatBot as cbot

# 音声認識オブジェクトを作成
r = sr.Recognizer()

def Speech_to_Text():
    # マイクから音声を録音
    with sr.Microphone() as source:
        print("話してください...")
        # 5秒間のタイムアウトを設定
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return(None)
        try:
            text = r.recognize_google(audio, language='ja-JP')
            return(text)
        except sr.UnknownValueError:
            return(None)
        except sr.RequestError as e:
            return(None)

def Main():
    # 音声を取得できるまで繰り返す
    print()
    for bot in cbot.ChatBot():
        print("bot：", bot)
        Call_Out.Call(bot) # 声を出す
        
        text = Speech_to_Text()
        if text is None:
            print("5秒間音声が検出されませんでした")
        else:
            print("you：", text)
            
        time.sleep(1)  # 1秒待機してから再度音声取得を試みる
    print()

print()    
text=Main()
print(text)
print()