from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route("/")
def home():
    return redirect('http://www.example.com')
