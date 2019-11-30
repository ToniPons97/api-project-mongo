from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from mongo_connect import db, coll
import json

@get("/data")
def index():
    return {dumps(coll.find())}


@get("/userNames")
def getUserNames():
    all_names = coll.find({}, {"idUser" : 1, "userName" : 1})
    for _ in all_names:
        return dumps(all_names)


@get("/userNames/<name>")
def getUserName(name):
    all_names = coll.find({}, {"userNamer" : 1})
    for i in all_names:
        if i == name:
            return dumps(i)


#@post('/add')
#def add():
 #   print(dict(request.forms))
  #  autor = request.forms.get("autor")
   # chiste = request.forms.get("chiste")  
    #return {
     #   "inserted_doc": str(coll.addChiste(autor,chiste))}


run(host='127.0.0.1', port=8080)

