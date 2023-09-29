from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
from datetime import datetime

from src.lib import joke
from src.lib.visma import getVisma
import json

app = Flask(__name__, template_folder="../frontend")  # Oppretter flask app
CORS(app)  # Flask CORS Står for Cross-Origin Resource Sharing som gjør at vi kan dele info mellom backend og frontend


@app.route('/')  # Index path
def index():
    return render_template("index.html")


# /<path:filename> gjør at HTML kan få tak i de statiske elementene
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory("../frontend", filename)


@app.route('/joke', methods=['GET'])  # En get request for joke API'en
def jokes():
    res = joke.getJoke()
    return res


@app.route('/visma', methods=['GET'])  # Get request for Visma API'en
def visma():
    def fetchAPI():
        timeplan = getVisma()
        if timeplan is None:
            fetchAPI()
        return timeplan
    timeplan = fetchAPI()
    timer = {}
    for i in range(len(timeplan)):
        timer[timeplan[i][1]] = timeplan[i][0]
    return timer


if __name__ == '__main__':
    # starter app i debug mode som gjør at den reloader serveren on save
    app.run(port=5000, debug=True, host="0.0.0.0")
