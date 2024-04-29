from flask import Flask, request 

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Error :) </h1>", 400



if __name__ == "main":
    app.run(debug=True)
