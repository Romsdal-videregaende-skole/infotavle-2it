from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
from datetime import datetime
from src.lib import joke, friminutt
from src.lib.visma import fetchAPI
import json

app = Flask(__name__, template_folder="../frontend")
CORS(app, resources={r"api/*": {"origins": "*"}})

@app.route('/')  # Index path
def index():
    return render_template("index.html")


# /<path:filename> gjør at HTML kan få tak i de statiske elementene
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory("../frontend", filename)

@app.route('/friminutt')
def getFriminutt():
    friminutt_start = ["9:5", "9:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
    friminutter = friminutt.liste(friminutt_start)
    print(friminutter)
    return {"friminutt": friminutter[1]/100}

  
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

    # starter app i debug mode som gjør at den reloader serveren on save
    app.run(port=5000, debug=True, host="0.0.0.0")

