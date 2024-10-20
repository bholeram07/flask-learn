from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to our page"

@app.route("/hello")
def hello():
    return "Hello i am bholeram"

from controller import user_controller