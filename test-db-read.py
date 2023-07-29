import pymongo
from db import client

# Pilih Database 1
db_name = 'iot_project'
db = client.get_database(db_name)

# Pilih collection
collection = db["data"]

# ambil data collection
result = collection.find()
for data in result:
    print(data)


