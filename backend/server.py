from flask import Flask
from flask_cors import CORS
from flask import request 
from markupsafe import escape
# so didnt realize that with flask im actually building an API rather than using REST or GraphQL or something
app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"

@app.route('/')
def index(): 
    return 'Index Page'

print(__name__)

if __name__ =='__main__':
    app.run() # note have this at the end, have the routes above it


# just run via python backend/server.py


