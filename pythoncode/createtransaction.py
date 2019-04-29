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
time = datetime.datetime.utcnow()
time2 = time.replace(tzinfo=pytz.UTC)
posix_now = int(time2.timestamp())                      #posix time

print("Enter your Email id:")
email=input()
print("Enter your Password:")
password=input()
records=db.reg_details.find({"email":email})
if(records.count()!=1):
    print("Not a valid user")
else:
    temp=list()
    temp1=list()
    print("Enter Hash Value:")
    hashvalue=input()
    for record in records:
        _id=str(record['_id'])
        publickey=record['public']
        privatekey=record['private']
        temp=record['transactions_owned']
        temp1=record['transactions_created']
    data_dict={'data':{'type':'PHD','hashvalue':hashvalue,'_id':_id,'date':posix_now}}
    print('creating transaction: {}'.format(data_dict))
    tx_metadata={'notes':'created transaction for '+email}
    prepared_create_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=publickey,
        asset=data_dict,
        metadata=tx_metadata
    )
    fulfilled_create_tx = bdb.transactions.fulfill(
        prepared_create_tx,
        private_keys=privatekey
    )
    sent_create_tx = bdb.transactions.send_commit(fulfilled_create_tx)
    print('CREATE transaction id: {}'.format(fulfilled_create_tx['id']))
    if(sent_create_tx == fulfilled_create_tx):
    	print("Success")
    	print(temp,temp1)
    	temp.append(fulfilled_create_tx['id'])
    	temp1.append(fulfilled_create_tx['id'])
    	db.reg_details.update({"email":email},{"$set":{'transactions_owned':temp,'transactions_created':temp1}})
