#!/usr/bin/python3
from pymongo import MongoClient
import getpass
import json
import os


client = MongoClient(os.getenv("URL"))


def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('api-project-mongo','chats')

with open('../input/chat.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)