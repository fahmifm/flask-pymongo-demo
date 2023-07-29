from flask import Flask, jsonify, request
from db import client

app = Flask(__name__)

# pilih database iot_project
db_name = 'iot_project'
db = client.get_database(db_name)

@app.route('/sensor')
def get_sensor_data():
    # pilih collection
    collection = db["data"]

    # ambil 1 data dengan temperature 100
    result = collection.find().sort("_id")
    result = list(result)
    if result:
        result = result[-1]
    else:
        result = None

    # return response
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)