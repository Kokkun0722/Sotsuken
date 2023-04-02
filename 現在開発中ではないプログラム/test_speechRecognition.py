import speech_recognition as sr
import Call_Out
import time
import test_chatbot as cbot

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
            # print("音声認識結果: " + text)
            return(text)
        except sr.UnknownValueError:
            # print("音声が認識できませんでした")
            return(None)
        except sr.RequestError as e:
            # print("エラーが発生しました: {0}".format(e))
            return(None)

def Main():
    # 音声を取得できるまで繰り返す
    print()
    for bot in cbot.ChatBot():
        print("bot：", bot)
        Call_Out.Call(bot)
        
        text = Speech_to_Text()
        if text is None:
            print("5秒間音声が検出されませんでした")
        else:
            print("you：", text)
            
        time.sleep(1)  # 1秒待機してから再度音声取得を試みる
    print()

print()    
text=Speech_to_Text()
print(text)
print()