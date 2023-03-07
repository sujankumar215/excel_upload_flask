from flask import Flask


app= Flask(__name__)

@app.route("/")
def welcome():
    return "Hello world"


@app.route("/home")
def home():
    return "this is home page"

#from controller import user_controller,product_controller
from controller import *

