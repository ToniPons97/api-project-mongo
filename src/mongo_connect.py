#!/usr/bin/python3
from dotenv import load_dotenv
import mongo
import json
import os
import dns

load_dotenv()

#Get Password
password = os.getenv("PASSWORD")
connection = f"mongodb+srv://toninopons:{password}@cluster0-ys9hj.mongodb.net/test?retryWrites=true&w=majority"
#Connect to DB
#client = MongoClient(connection)
connection_return = mongo.CollConection("api-project-mongo", "Chats")

with open('../input/chat.json') as f:
    chats_json = json.load(f)
mongo.CollConection.addManyDocuments(chats_json)
