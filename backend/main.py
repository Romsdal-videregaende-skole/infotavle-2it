from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
from datetime import datetime
from src.lib import joke
from src.lib import friminutt
from src.lib.visma import getVisma
import json


app = Flask(__name__, template_folder="../frontend")  # Oppretter flask app
CORS(app)  # Flask CORS Står for Cross-Origin Resource Sharing som gjør at vi kan dele info mellom backend og frontend


@app.route('/')  # Index path
def index():
    return render_template("index.html")


@app.route('/friminutt', methods=['GET'])
def getFriminutt():
    
    def liste(friminutt):
        today = datetime.now()
        current_time = datetime.now().time()

        for x in range(len(friminutt)):
            split_tider = friminutt[x].split(":")
            res = [eval(i) for i in split_tider]
            test = datetime(today.year, today.month, today.day, res[0], res[1])
            if today < test:
                current_datetime = datetime.combine(datetime.today(), current_time)
                time_difference = test - current_datetime
                total_minutes_until_recess = time_difference.total_seconds() / 60
                percentage_difference = (total_minutes_until_recess / 40) * 100

                # Invert the percentage
                inverted_percentage = 100 - percentage_difference

                return friminutt[x], inverted_percentage
            

    # Calculate the break times within the route handler
    friminutt_start = ["9:5", "9:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
    friminutter = liste(friminutt_start)
    return {"friminutt": friminutter[1]}

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

