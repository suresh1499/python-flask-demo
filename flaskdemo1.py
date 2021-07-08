from flask import Flask

app = Flask(__name__)
# http://localhost:8080/
@app.route("/")
def welcome():
    return "My First Api"
