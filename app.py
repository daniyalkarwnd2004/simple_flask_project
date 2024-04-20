from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name = "daniyal"
    return "Hello " + name