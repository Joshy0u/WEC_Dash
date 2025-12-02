from flask import Flask
from flask_cors import CORS
from flask import request 
from markupsafe import escape
from routes.routes import routes_bp
# so didnt realize that with flask im actually building an API rather than using REST or GraphQL or something
app = Flask(__name__)

app.register_blueprint(routes_bp)


if __name__ =='__main__':
    app.run() # note have this at the end, have the routes above it


# just run via python backend/server.py


