from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Travis Williams in 3308.'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://helloworld_postgres_db_user:rZTZIbAl6f6clBALIpNHipv16Qogi3xn@dpg-d481leemcj7s73dmeuhg-a/helloworld_postgres_db")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgresql://helloworld_postgres_db_user:rZTZIbAl6f6clBALIpNHipv16Qogi3xn@dpg-d481leemcj7s73dmeuhg-a/helloworld_postgres_db")
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
    return "Basketball table created successfully."
