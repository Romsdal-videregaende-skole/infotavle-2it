from flask import Flask, send_from_directory
from flask_cors import CORS
import json
from src.lib import joke
from src.lib import friminutt

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory("src/pages", "index.html")


@app.route('/friminutt')
def getFriminutt():
    friminutt_start = ["9:5", "9:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
    friminutter = friminutt.liste(friminutt_start)
    print(friminutter)
    return {"friminutt": friminutter[1]/100}

@app.route('/joke', methods=['GET'])
def jokes():

    res = joke.getJoke()
    return res

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")