from flask import Flask
from forms import NameForm
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


from app import app
bootstrap = Bootstrap(app)
app.config ["SECRET_KEY"] = "WElcome To Web"


@app.route("/", methods=["POST", "GET"])
def home():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return  render_template("home.html", form = form, name = name)