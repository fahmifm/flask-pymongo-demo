import pymongo

# bikin koneksi ke mongodb 
# ganti url sesuai url dari atlas mongodb
username = ""
password = ""
db_host = ""
client = pymongo.MongoClient("mongodb+srv://{username}:{password}@{db_host}/?retryWrites=true&w=majority".format(username=username, password=password, db_host=db_host))

# pilih database iot_project, sesuaikan dengan database yg kalian bikin
# contoh : db_name = 'kelompok_123'
db_name = ''
db = client.get_database(db_name)

# pilih collection
collection = db["data"]

# ambil data collection
result = collection.find()
for data in result:
    print(data)

# ambil satu data
# result = collection.find_one({"temperature": 100})
# print(result)

