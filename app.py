from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing:
    conn = psycopg2.connect("postgres://brbi1248_db_user:cnQbJbn0p8hK9SFfSVJ10oBYUhFkMVEv@dpg-cgcug2m4dad6fr7dvs20-a/brbi1248_db")
    conn.close()
    return "Database Connection was successful"