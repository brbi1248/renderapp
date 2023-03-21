from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://brbi1248_db_user:cnQbJbn0p8hK9SFfSVJ10oBYUhFkMVEv@dpg-cgcug2m4dad6fr7dvs20-a/brbi1248_db")
    conn.close()
    return "Database Connection Successful"
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://brbi1248_db_user:cnQbJbn0p8hK9SFfSVJ10oBYUhFkMVEv@dpg-cgcug2m4dad6fr7dvs20-a/brbi1248_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"