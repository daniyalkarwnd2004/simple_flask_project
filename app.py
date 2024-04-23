from flask import Flask

app = Flask(__name__)

@app.route("/user/<int:id>")
def home(id):
    return f"welcome user id {id}"