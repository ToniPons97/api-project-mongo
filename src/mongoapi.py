#!/usr/local/bin/python3
from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from mongo_connect import db, coll
import json
import pandas

@get("/data/")
def index():
    return {dumps(coll.find())}


@get("/userNames/")
def getUserNames():
    all_names = coll.find({}, {"idUser" : 1, "userName" : 1})
    return (dumps(all_names))

@get("/text/")
def getAllChats():
    all_chats = coll.find({}, {"text" : 1})
    for _ in all_chats:
        return (dumps(all_chats))


@get("/userNames/<name>")
def getUserName(name):
    names = coll.find({}, {"idUser" : 1, "userName" : 1})
    person = [p for p in names if p['userName'] == name]
    return dumps(person)




#@post('/add')
#def add():
 #   print(dict(request.forms))
  #  autor = request.forms.get("autor")
   # chiste = request.forms.get("chiste")  
    #return {
     #   "inserted_doc": str(coll.addChiste(autor,chiste))}


run(host='127.0.0.1', port=8080)

