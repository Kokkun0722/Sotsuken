import pyttsx3
    
# 喋らせる言葉　例えば「時間に応じて、こんな時間にお出かけですか？のような声掛けを行ないたい」「家族に通知を入れたい」。
message="はい、チーズ。"
engine = pyttsx3.init()

def Call():
    #喋らせる
    engine.say(message)
    engine.runAndWait()