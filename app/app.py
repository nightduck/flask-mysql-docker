from flask import Flask
import mysql.connector

app = Flask(__name__)

passwd_fin = open("/run/secrets/db-password", 'r')
password = passwd_fin.readline()

config = {
        'user': 'root',
        'password': password,
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
