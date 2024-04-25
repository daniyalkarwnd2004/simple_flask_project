from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/user/<name>")
def name(name):
    return f"<h1>Hello {name}</h1>"

if __name__ == "main":
    app.run(debug=True)