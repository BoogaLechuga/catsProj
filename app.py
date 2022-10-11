from flask import Flask

app = Flask(__name__)

@app.route("/")

def cats() :
    return{"message":"cats!"}