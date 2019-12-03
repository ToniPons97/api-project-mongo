#!/usr/local/bin/python3
import random
import json
import nltk
from bottle import route, run, get, post, request
from bson.json_util import dumps
from mongo_connect import connectCollection
from nltk.sentiment.vader import SentimentIntensityAnalyzer

db, coll = connectCollection("api-project-mongo", "Chats")

@get("/data")
def index():
    return {dumps(coll.find())}


@get("/userNames")
def getUserNames():
    all_names = coll.find({}, {"idUser" : 1, "userName" : 1, "idChat" : 1})
    return (dumps(all_names))


@get("/chats")
def getAllChats():
    #get all chats

    return dumps(coll.find({}, {"text" : 1}))


@get("/userNames/<name>")
def getUserName(name):
    """
    get all chats and messages for a particular user
    """
    return dumps(coll.find({"userName" : name}))

  
@get("/userNames/<name>/limit=<number>")
def getUserNameLimit(name, number):
    """
    get number of chats and messages for a particular user
    """
    number = int(number)
    return dumps(coll.find({"userName" : name}).limit(number))


@get("/chats/limit=<number>")
def getTextsWithLimit(number):
    """
    limit results of chats get request
    """
    number = int(number)
    texts = coll.find({}, {"idUser" : 1, "userName" : 1, "text" : 1, "idChat" : 1}).limit(number)
    return dumps(texts)


@get("/chat/<number>")
def getSpecificChat(number):
    """
    get specific chat entering idChat
    """
    number = int(number)
    return dumps(coll.find({"idChat" : number}))


@get("/overall_sentiment")
def sentiments():
    """
    get sentiment analysis of all messages
    """
    sentiment = dict()
    text = ""
    sid = SentimentIntensityAnalyzer()

    for e in coll.find():
        try:
            text += e["text"] + " "
            sentiment['analysis'] = sid.polarity_scores(text)
        except:
            pass
    return sentiment


@get("/sentiment/chat=<number>")
def sentimentSpecificChat(number):
    """
    get sentiment analysis for a specific chat
    """
    number = int(number)
    sentiment = dict()
    text = ""
    sid = SentimentIntensityAnalyzer()
    
    for e in coll.find({"idChat" : number}):
        try:
            text += e["text"] + " "
            sentiment["analysis"] = sid.polarity_scores(text)
        except:
            pass
    return sentiment


@get("/sentiment/<user>")
def sentimentSpecificUser(user):
    """
    get sentiment analysis for specific user
    """
    sentiment = dict()
    text = ""
    sid = SentimentIntensityAnalyzer()

    for e in coll.find({"userName" : user}):
        try:
            text += e["text"] + " "
            sentiment["analysis"] = sid.polarity_scores(text)
        except:
            pass
    return sentiment


@post('/user/create')
def newUser():
    """
    add new user to the database. This new user won't have any messages or chats
    """
    name = str(request.forms.get("userName"))
    new_id = max(coll.distinct("idUser")) + 1
    names = coll.distinct("userName")
    if name in names:
        return "name already in database"
    else:
        new_user = {
            "idUser": new_id,
            "userName": name
        }
        coll.insert_one(new_user)
        print(f"{name} added to collection with id {new_id}")
        return f"user_id {new_id}"


@post("/chat/create")
def createChat():
    """
    create a chat with exsting users
    """
    c = max(coll.distinct("idChat"))+1
    users_list = list(request.forms.getall("idUser"))
    print(users_list)
    info = []
    for u in users_list:
        user = {}
        user_info = (coll.find({"idUser":int(u)},{"userName":1}))
        print(user_info)
        user["idUser"] = u
        user['userName'] = user_info[0]["userName"]
        user['idChat'] = c
        print(user)
        info.append(user)
    coll.insert_many(info)
    return f"Chat_id: {c}"


run(host='127.0.0.1', port=8080)

