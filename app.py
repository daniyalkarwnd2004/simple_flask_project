from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    user = "dani"
    commit = ["welcome", "hello", "good"]
    return render_template("index.html", user=user, commit=commit)
