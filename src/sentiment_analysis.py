from mongo_connect import connectCollection
from bson.json_util import dumps
from bottle import route, run, get, post, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
import json


all_conversations = ""


for i in range(5):
    res = requests.get(f"http://localhost:8080/chat/{i}").json()   
    for i in range(len(res)):
        try:
            all_conversations += " " + res[i]["text"]
        except:
            pass

print(all_conversations)

"""
def getSentiment():
    text = []
    scores = {}
    x = list(coll.find())
    for i in range(len(x)):
        try:
            text.append(x[i]["text"])
        except:
            pass
    #for i in text:
     #   scores["score"] = (sid.polarity_scores(text))
    return text
"""

#sentence = "FUCK YOU"
#sid = SentimentIntensityAnalyzer()
#print(sid.polarity_scores(sentence))
