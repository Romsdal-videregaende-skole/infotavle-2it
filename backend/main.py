from flask import Flask, send_from_directory
import json


app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory("src/pages", "index.html")

if __name__ == '__main__':
    app.run(port=5500, debug=True)