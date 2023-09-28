from flask import Flask, send_from_directory, url_for, render_template
from flask_cors import CORS
import json
from src.lib import joke

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

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")