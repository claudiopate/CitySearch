from flask import Flask
from flask_cors import CORS #comment this on deployment

import json
import sys
sys.path.append('api/')
import search_docs as sd


app = Flask(__name__)
CORS(app)

@app.route('/')
def home_page():
    return 'Home'

@app.route('/search/<city>')
def search_by_city(city):
    cities = sd.search(city)
    return json.dumps(cities)


if __name__ == '__main__':

    #Start Server
    app.run(host='0.0.0.0', debug=True, use_reloader=True)