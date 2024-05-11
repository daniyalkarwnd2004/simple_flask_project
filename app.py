from os import name
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for


app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/<name>")
def user():
    return render_template("index.html")

if __name__ == 'main':
    app.run(debug=True)

