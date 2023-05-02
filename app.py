from flask import Flask

app = Flask(__name__)

@app.route("/pathfinder")
def hello():
    return "Hello, welcome to Pathfinder!"

    