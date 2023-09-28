from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
import json
from src.lib import joke
from src.lib.visma import getVisma

app = Flask(__name__, template_folder="../frontend")
CORS(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory("../frontend", filename)

@app.route('/joke', methods=['GET'])
def jokes():

    res = joke.getJoke()
    return res

@app.route('/visma', methods=['GET'])
def visma():
    def fetchAPI():
        timeplan = getVisma()
        if timeplan is None:
            fetchAPI()
        return timeplan
    timeplan = fetchAPI()
    timer = {}


    for i in range(len(timeplan)):
        timeplan[i][1] = timeplan[i][0]

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")