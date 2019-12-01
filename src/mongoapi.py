#!/usr/local/bin/python3
from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from mongo_connect import connectCollection
import json

db, coll = connectCollection("api-project-mongo", "Chats")

@get("/data/")
def index():
    return {dumps(coll.find())}


@get("/userNames/")
def getUserNames():
    all_names = coll.find({}, {"idUser" : 1, "userName" : 1, "idChat" : 1})
    return (dumps(all_names))


@get("/text/")
def getAllChats():
    return dumps(coll.find({}, {"text" : 1}))


@get("/userNames/<name>/")
def getUserName(name):
    return dumps(coll.find({"userName" : name}))
    


@get("/text/limit=<number>/")
def getTextsWithLimit(number):
    number = int(number)
    texts = coll.find({}, {"idUser" : 1, "userName" : 1, "text" : 1, "idChat" : 1}).limit(number)
    return dumps(texts)





#@post('/add')
#def add():
 #   print(dict(request.forms))
  #  autor = request.forms.get("autor")
   # chiste = request.forms.get("chiste")  
    #return {
     #   "inserted_doc": str(coll.addChiste(autor,chiste))}


run(host='127.0.0.1', port=8080)

