from bigchaindb_driver.crypto import generate_keypair
sample=generate_keypair()
print(sample.private_key)
print(sample.public_key)
