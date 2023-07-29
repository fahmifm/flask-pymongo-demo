import pymongo # meng-import library pymongo yang sudah kita install
from flask import Flask, request

# inisiasi Flask
app = Flask(__name__)

# Buat Koneksi database
username = "user db kalian"
password = "password db kalian"
db_hostname = "test-cluster.dskfj.mongodb.net"
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{db_hostname}/GettingStarted?retryWrites=true&w=majority")

# Pilih Database sesuai kelompok
database_name = "nama database kalian"
db = client[database_name] 

# Pilih collections
collection_name = "nama collection kalian"
my_collections = db[collection_name] 

@app.route('/sensor1', methods=["POST"])
def insert_data():
    # Untuk insert data ke database
    # mengolah data dari JSON data POST
    data = request.get_json()

    # Insert data ke database
    my_collections.insert_one(data)

    return 'Sukses gan!'

@app.route('/sensor1/temperature/avg', methods=["GET"])
def temperature_avg():
    # query ke database mengambil data temperature
    data = my_collections.find()
    
    # hitung average
    temperature_data = []
    for d in data:
        temperature_data.append(d["suhu"])
    print(temperature_data)
    
    average = sum(temperature_data)/len(temperature_data)

    return 'AVG temperature = {}'.format(average)

@app.route('/sensor1/kelembapan/avg', methods=["GET"])
def kelembapan_avg():
    # query ke database mengambil data kelembapan
    data = my_collections.find()

    # hitung average
    kelembapan_data = []
    for d in data:
        kelembapan_data.append(d["kelembapan"])
    print(kelembapan_data)
    
    average = sum(kelembapan_data)/len(kelembapan_data)
    return 'AVG kelembapan = {}'.format(average)

if __name__ == '__main__':
    app.run(debug=True)



