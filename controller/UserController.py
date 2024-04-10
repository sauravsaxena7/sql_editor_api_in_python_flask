from app import app

from model.QueryModel import QueryModel
from flask import request

obj = QueryModel()
@app.route("/query/ExecuteQuery",methods=["POST"])
def ExecuteQuery():
    return obj.ExecuteQuery(request.json)

@app.route("/query/createDatabase",methods=["POST"])
def CreateNewDatabase():
    return obj.CreateNewDatabase(request.json)   

@app.route("/query/GetAllDatabase",methods=["GET"])
def GetAllDatabase():
    return obj.GetAllDatabase()        
