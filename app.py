from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def home(name):
    return "<h1>Welcome, %s! </h1>" % name