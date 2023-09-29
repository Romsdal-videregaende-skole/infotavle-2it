from flask import Flask, send_from_directory
from flask_cors import CORS
from datetime import time as Time
from datetime import datetime, time
import json
from src.lib import joke

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory("src/pages", "index.html")


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

@app.route('/joke', methods=['GET'])
def jokes():

    res = joke.getJoke()
    return res

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")