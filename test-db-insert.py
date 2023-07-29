import pymongo
from db import client

# Pilih Database 1
db_name = 'iot_project'
db = client.get_database(db_name)

# Pilih collection
collection = db["data"]

# insert data
data = {
    "suhu": 95,
    "kelembapan": 71
}
collection.insert_one(data)


