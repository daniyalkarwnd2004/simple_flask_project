from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap = Bootstrap(app)


@app.route("/<name>")
def home(name):
    user = name
    return render_template("index.html", name = user)
