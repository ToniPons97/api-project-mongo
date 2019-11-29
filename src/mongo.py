#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
import os

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://toninopons:{}@cluster0-ys9hj.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('api-project-mongo','Chats')

with open('~/Documents/Projects/api-project-mongo/input/chats.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)