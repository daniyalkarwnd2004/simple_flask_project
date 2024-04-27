from flask import Flask, request 

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = request.headers.get('user_agent')
    return f'your browser is :{user_agent}'
if __name__ == "main":
    app.run(debug=True)