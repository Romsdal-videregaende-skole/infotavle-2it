from flask import Flask, send_from_directory, render_template
from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
from datetime import datetime
from src.lib import joke, friminutt, weather
from src.lib.visma import getVisma
import json

app = Flask(__name__, template_folder="../frontend")
# Initialize flask Cors (Cross Origin Resource Sharing) on only the /api/* URI endpoints
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')  # Index path
def index():
    return render_template("index.html")


# /<path:filename> gjør at HTML kan få tak i de statiske elementene
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory("../frontend", filename)


@app.route('/api/friminutt', methods=['GET'])
def getFriminutt():

    def liste(friminutt):
        today = datetime.now()
        current_time = datetime.now().time()

        for x in range(len(friminutt)):
            split_tider = friminutt[x].split(":")
            res = [eval(i) for i in split_tider]
            test = datetime(today.year, today.month, today.day, res[0], res[1])
            if today < test:
                current_datetime = datetime.combine(
                    datetime.today(), current_time)
                time_difference = test - current_datetime
                total_minutes_until_recess = time_difference.total_seconds() / 60
                percentage_difference = (total_minutes_until_recess / 40) * 100

                # Invert the percentage
                inverted_percentage = 100 - percentage_difference

                return friminutt[x], inverted_percentage

    # Calculate the break times within the route handler
    friminutt_start = ["9:5", "9:55", "10:55",
                       "11:45", "13:00", "13:50", "14:40"]
    friminutter = liste(friminutt_start)
    print(friminutter)
    return {"friminutt": "friminutter[1]"}


@app.route('/api/joke', methods=['GET'])
def jokes():
    res = joke.getJoke()
    return res


@app.route('/api/visma', methods=['GET'])
def visma():
    return getVisma()


@app.route('/api/weather', methods=['GET'])
def getWeather():
    return {"temp": weather.temperature()}


if __name__ == '__main__':

    # starter app i debug mode som gjør at den reloader serveren on save
    app.run(port=8080, debug=True, host="0.0.0.0")
