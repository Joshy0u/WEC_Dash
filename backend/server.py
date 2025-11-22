from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

if __name__ =='__main__':
    app.run()

print(__name__)



@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
