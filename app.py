from datetime import datetime
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for
from flask import request
from flask_moment import Moment



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config["SECRET_KEY"] = "hi dani hello your is is welcome "


@app.route("/")
def page_one():
    return render_template("serch.html")


@app.route("/home")
def home_page():
    time = datetime.utcnow()
    return render_template("home.html", time = time)


@app.route("/home/<user>")
def home_page2(user):
    time = datetime.utcnow()
    return render_template("home.html", user= user, time=time)



@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/usersystemprofile")
def user_pofile():
    agent = request.headers.get("user_agent")
    return render_template("usersystemprofile.html", agent=agent)


@app.route("/comments")
def comment():
        user = {"name": "dani"}
        posts = [
        {
            'author': {"username":"neda"},
            'body':"beautiful day in portland"
         },

         {
            'author':{"username":"ali"},
            'body': "the avengers movie was os cool !"
          }
    ]
        return render_template("comments.html",user = user, posts = posts)
    

@app.errorhandler(404)
def Error_404(e):
    return render_template("404.html", title = "error 404"), 404


@app.errorhandler(500)
def Error500(e):
    
    return render_template("500.html", title = "error 500"), 500

if __name__ == "__main__":
    app.run()
