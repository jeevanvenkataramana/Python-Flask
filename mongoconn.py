import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient()
db=client.bigchain
# Issue the serverStatus command and print the results
records=db.assets.find()

print(type(records))
for record in records:
	print(type(record))
