from flask import Flask, send_from_directory, render_template
from flask_cors import CORS
import json
from src.lib import joke

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/joke', methods=['GET'])
def jokes():

    res = joke.getJoke()
    return res

if __name__ == '__main__':
    app.run(port=5000, debug=True)