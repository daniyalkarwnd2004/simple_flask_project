from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<username>")
def user(username):
    return render_template("userstyle.html", username = username)

