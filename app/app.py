from flask import Flask
import mysql.connector

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'enterpasswordhere',
        'host': 'db',
        'port': '3306',
        'database': 'dms_db'
    }
connection = mysql.connector.connect(**config)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
