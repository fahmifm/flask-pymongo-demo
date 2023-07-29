import pymongo

USER = ""
PASS = ""
DB_HOST = ""

client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASS}@{DB_HOST}/?retryWrites=true&w=majority&ssl=true")
db = client.test
test_collection = db.test_collection
# test_collection = db.create_collection("test_collection")
result = test_collection.insert_one({"name": "wedhus"})
print(result)
