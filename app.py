from flask import Flask
from flask import render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment 


app = Flask(__name__)
from app import app
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def home():
    time = datetime.utcnow()
    return render_template("home.html", time = time)

@app.route("/song")
def song():
    time = datetime.utcnow()
    return render_template("happy_song.html", time=time)

@app.route("/special")
def special():
    time = datetime.utcnow()
    return render_template("special_songs.html", time=time)


@app.route("/remex")
def remex():
    time = datetime.utcnow()
    return render_template("remex.html", time = time)

@app.errorhandler(404)
def Error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def Error_500():
    return render_template("500.html"), 500



if __name__ == "main":
    app.run(debug=True)
