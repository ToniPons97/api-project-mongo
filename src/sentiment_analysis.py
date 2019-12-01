from mongo_connect import connectCollection
from bson.json_util import dumps
from bottle import route, run, get, post, request
import textblob

db, coll = connectCollection("api-project-mongo", "Chats")

@get("/sentiment/")
def getSentiment():
    for i in dumps(coll.find()):
        return i["text"]

run(host="127.0.0.1", port=8080)
