from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({"Index": "main"})

if __name__ == '__main__':
    app.run(5500, debug=True)