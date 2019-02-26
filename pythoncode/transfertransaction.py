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
    	print("Enter The Transaction that needs to be transfered")
    	tx_id=input()
    	if(tx_id in record['transactions_owned']):
    		print("Enter email id of the user the asset needs to be transfered:")
    		newuser_email=input()
    		details=db.reg_details.find({"email":newuser_email})
    		if(details.count()==1):
    			for detail in details:
    				publickey1=detail['public']
    				time = datetime.datetime.utcnow()
    				time2 = time.replace(tzinfo=pytz.UTC)
    				posix_now = int(time2.timestamp())
    				asset_to_transfer = {'id': tx_id}
    				transfer_tx_metadata = {'notes': 'Transfer, from '+email+' to '+newuser_email,'new_owner': newuser_email,'transfer_time': posix_now}
    				print('TRANSFER tx metadata: {}'.format(transfer_tx_metadata))
    				creation_tx = bdb.transactions.retrieve(tx_id)
    				output = creation_tx['outputs'][0]
    				transfer_input={'fulfills':{'transaction_id': tx_id,'output_index': 0},'owners_before': [publickey],'fulfillment': output['condition']['details']}
    				prepared_transfer_tx = bdb.transactions.prepare(operation='TRANSFER',asset=asset_to_transfer,metadata=transfer_tx_metadata,inputs=transfer_input,recipients=publickey1)
    				fulfilled_transfer_tx = bdb.transactions.fulfill(prepared_transfer_tx,private_keys=privatekey)
    				sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
    				print('Successfull TRANSFER tx id: {}'.format(fulfilled_transfer_tx['id']))
    				transactions_owned=record['transactions_owned']
    				transactions_owned.remove(tx_id)
    				db.reg_details.update({"email":email},{"$set":{'transactions_owned':transactions_owned}})
    				transactions_owned.clear()
    				transactions_owned=detail['transactions_owned']
    				transactions_owned.append(fulfilled_transfer_tx['id'])
    				db.reg_details.update({"email":newuser_email},{"$set":{'transactions_owned':transactions_owned}})
    		else:
    			print("Enter a Valid User Email")
    	else:
    		print("Enter a Valid Transaction Id")
