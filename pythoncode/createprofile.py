from bigchaindb_driver.crypto import generate_keypair
import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient()
db=client.user_data
# Issue the serverStatus command and print the results
print("Enter User Name:")
username=input()
print("Enter Email:")
email=input()
print("Enter Password:")
password=input()
sample=generate_keypair()
private=sample.private_key
public=sample.public_key
print("{} {} {} {} {}".format(username,email,password,private,public))
data={'username':username,'email':email,'password':password,'private':private,'public':public}
result=db.reg_details.insert_one(data)
print('Created with id {}'.format(result.inserted_id))
