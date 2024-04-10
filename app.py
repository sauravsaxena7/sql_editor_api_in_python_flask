from flask import Flask
from flask_cors import CORS, cross_origin

app=Flask(__name__)
CORS(app, support_credentials=True)


#DECORATOR
@app.route("/")
def welcome():
    return "HELLO WORLD"




from controller import *
