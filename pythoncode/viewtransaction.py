import datetime
import pytz
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import pymongo
from pymongo import MongoClient


bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)
client = pymongo.MongoClient()
db=client.user_data
db1=client.bigchain

print("Enter your Email id:")
email=input()
print("Enter your Password:")
password=input()
records=db.reg_details.find( { "$and": [ {"email":email},{"password":password} ] } )
if(records.count()!=1):
    print("Not a valid user")
else:
    print("Successful", records.count())
    for record in records:
        publickey=record['public']
        privatekey=record['private']
        print("List of transactions created:")
        print(record['transactions_created'])
        print("Transactions Currenlty Owned:")
        print(record['transactions_owned'])

