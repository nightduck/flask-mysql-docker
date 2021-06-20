import flask
import mysql.connector
import datetime
import re

app = flask.Flask(__name__)

#passwd_fin = open("/run/secrets/db-password", 'r')
#password = passwd_fin.readline()
password = "enterpasswordhere"

config = {
        'user': 'root',
        'password': password,
        'host': 'db',
        'port': '3306',
        'database': 'dms_db'
    }

@app.route('/')
def home_page():
    return 'Hello World!'

@app.route('/user/<user_id>')
def greet_user(user_id):
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("SELECT Birthday, FirstName, LastName FROM birthdays WHERE ID=%s;" % (user_id))
    row = cur.fetchone()

    cur.close()
    connection.close()

    return_str = "Hello %s %s" % (row[1], row[2])

    today = datetime.date.today()
    if row[0] == today:
        return_str += "\nHappy birthday!"

    return return_str

@app.route('/create_user/<first>/<last>/<birthday>', methods=['POST'])
def create_user(first, last, birthday):
    try:
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        err = flask.Response(status=400)
        return err

    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    query = 'INSERT INTO birthdays(Firstname, LastName, Birthday) VALUES ("%s", "%s", "%s");' % (first, last, str(birthday))
    try:
        cur.execute(query)
    
        connection.commit()
    except:
        cur.close()
        connection.close()
        return query

    cur.close()
    connection.close()

    return flask.Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
