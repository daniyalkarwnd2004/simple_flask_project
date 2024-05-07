from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap = Bootstrap(app)


@app.route("/")
def home():
    user = "dani"
    commit = ["welcome", "hello", "good"]
    return render_template("index.html", user=user, commit=commit)
