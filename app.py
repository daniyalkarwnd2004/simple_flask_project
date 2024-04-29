from flask import Flask, request 
from flask import make_response

app = Flask(__name__)


@app.route("/")
def home():
    response = make_response("hello :)")
    response.set_cookie("jhon", "42")
    return response



if __name__ == "main":
    app.run(debug=True)
