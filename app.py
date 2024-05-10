from os import name
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for


app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return "gggg"


@app.route("/user/<name>")
def user(name):
    return f"welcome {name}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('user', name=name))
