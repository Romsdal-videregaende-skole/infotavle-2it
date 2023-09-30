from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
from datetime import datetime

from src.lib import joke
from src.lib.visma import getVisma, fetchAPI
import json

app = Flask(__name__, template_folder="../frontend")
CORS(app, resources={r"api/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory("../frontend", filename)


@app.route('/api/joke', methods=['GET'])
def jokes():

    res = joke.getJoke()
    return res


@app.route('/api/visma', methods=['GET'])
def visma():

    timeplan = fetchAPI()
    timer = {}
    for i in range(len(timeplan)):
        timer[timeplan[i][1]] = timeplan[i][0]
    return timer


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
