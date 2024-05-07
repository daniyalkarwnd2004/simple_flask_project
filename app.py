from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def username(name):
    user = name
    return render_template("index.html", name = user)
