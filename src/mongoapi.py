from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from mongo_connect import db, coll
import json

@get("/data")
def index():
    return {dumps(coll.find())}


@get("/userNames")
def demo2():
    names = coll.find({}, {'idUser': 1, 'userName':1})
    for _ in names:
        return dumps(names)

#@post('/add')
#def add():
 #   print(dict(request.forms))
  #  autor = request.forms.get("autor")
   # chiste = request.forms.get("chiste")  
    #return {
     #   "inserted_doc": str(coll.addChiste(autor,chiste))}


run(host='127.0.0.1', port=8080)

