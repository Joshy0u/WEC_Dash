from flask import jsonify, Blueprint
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from fileParser import load_parsed_data
from fileParser import load_parsed_data

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def index():
    return jsonify(message="Hello Front Page!")
    # returns a msg in json format

@routes_bp.route('/Hello')
def hello():
    return "Hello from the /Hello route!"

@routes_bp.route('/data')
def data():
    sample_data = {
        "name": "WEC DASH",
        "version": 1.0, 
        "features":["NONE!", "LITERALLY", "NOTHING", "HERE"]
    }
    return jsonify(sample_data)

@routes_bp.route('/parsed-data')
def parsed_data():
    data = load_parsed_data()
    return jsonify(data)