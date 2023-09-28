from flask import Flask, send_from_directory
import json
from src.lib import joke

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory("src/pages", "index.html")


@app.route('/joke', methods=['GET'])
def jokes():
    while True:
        res = joke.getJoke()
        return res

if __name__ == '__main__':
    app.run(port=5500, debug=True)