from mongo_connect import connectCollection
from bson.json_util import dumps
from bottle import route, run, get, post, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



db, coll = connectCollection("api-project-mongo", "Chats")

@get("/sentiment/")
def getSentiment():
    text = ""
    for e in dumps(coll.find()):
        text += + e["text"] + " "   

    print(text)
    return dumps(coll.find())

run(host="127.0.0.1", port=8080)


#sentence = "FUCK YOU"
#sid = SentimentIntensityAnalyzer()
#print(sid.polarity_scores(sentence))
