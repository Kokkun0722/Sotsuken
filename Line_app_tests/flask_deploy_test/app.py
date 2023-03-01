from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello():
    return "(^▽^)"

if __name__ == "__main__":
    #app.run('0.0.0.0',port=5000)
    serve(app, host='0.0.0.0', port=5000)
    
# http://127.0.0.1:5000/