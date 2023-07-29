from flask import Flask, jsonify, request
from db import client

app = Flask(__name__)

# pilih database iot_project
db_name = ''
db = client.get_database(db_name)

@app.route('/makan')
def minta_makan():
    # pilih collection
    collection = db["sensor"]

    # ambil 1 data dengan temperature 100
    result = collection.find_one({"temperature": 100}, {"_id": 0})

    # return response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)