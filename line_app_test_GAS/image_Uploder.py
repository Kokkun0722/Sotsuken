import gspread
from oauth2client.service_account import ServiceAccountCredentials
import cv2
from datetime import datetime

# Google Sheets API情報
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/service_account_key.json', scope)
client = gspread.authorize(creds)

# スプレッドシートの情報
sheet = client.open('Spreadsheet Name').sheet1

# カメラから写真を取得する
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# 日時を取得する
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# スプレッドシートにデータを追加する
row = [dt_string, 'file_name.jpg']
sheet.append_row(row)

# ファイルを保存する
cv2.imwrite('file_name.jpg', frame)

# カメラを解放する
cap.release()
cv2.destroyAllWindows()