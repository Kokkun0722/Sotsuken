import speech_recognition as sr

# 音声認識オブジェクトを作成
r = sr.Recognizer()

# マイクから音声を録音
with sr.Microphone() as source:
    print("話してください...")
    audio = r.listen(source)

# 音声をテキストに変換
try:
    text = r.recognize_google(audio, language='ja-JP')
    print("音声認識結果: " + text)
except sr.UnknownValueError:
    print("音声が認識できませんでした")
except sr.RequestError as e:
    print("エラーが発生しました: {0}".format(e))

print()