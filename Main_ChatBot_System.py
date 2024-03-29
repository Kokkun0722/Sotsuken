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
            audio = r.listen(source, timeout=5, phrase_time_limit=2)
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
    manual=["君の運命の人は僕じゃない","つらいけど否めない","でも離れたくないのさ"]
    finish="それでは、いってらっしゃいませ。"
    
    # manual=cbot.ChatBot()
    memory=[]
    # 音声を取得できるまで繰り返す
    print()
    for bot in manual:
        print("bot：", bot)
        memory.append("bot："+bot)
        Call_Out.Call(bot) # 声を出す
        
        text = Speech_to_Text()
        if text is None:
            print("2秒間音声が検出されませんでした")
        else:
            print("you：", text)
            memory.append("you："+text)
            
        time.sleep(0.1)  # 1秒待機してから再度音声取得を試みる
    Call_Out.Call(finish)
    print("bot：",finish)
    memory.append("bot："+ finish)
    print()
    return memory

Main()