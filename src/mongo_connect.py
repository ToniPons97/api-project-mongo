#!/usr/bin/python3
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("URL"))


def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

#db, coll = connectCollection("api-project-mongo", "Chats")

#with open("../input/chat.json") as f:
#    chats_json = json.load(f)
#coll.insert_many(chats_json)
