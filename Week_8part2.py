
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql
from flask_json import json_response

#from flask_mysqldb import MySQL


app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/netflix'

res = []

db = mysql.connect(
    # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
    host = "db", # would be localhost if not running in docker
    user = "root",
    passwd = "root",
    db = "netflix"
    #,charset='latin1'
    #,collation='latin1_danish_ci'
)


cur = db.cursor()
query = 'select * from netflix where release_year = 2000'
cur.execute(query)

result = cur.fetchall()



@app.route('/api/get-data', methods=['GET'])
def response():
    for m in result:
        res.append(m)
    return jsonify(res)


@app.route('/')
def home():
    return "hello"
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql
#from flask_mysqldb import MySQL


app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/netflix'

response = []

db = mysql.connect(
    # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
    host = "localhost", # would be localhost if not running in docker
    user = "root",
    passwd = "root",
    db = "netflix"
    #,charset='latin1'
    #,collation='latin1_danish_ci'
)


cur = db.cursor()
query = 'select * from netflix where release_year = 2000'
cur.execute(query)

myresult = cur.fetchall()

for x in myresult:
    response.append(x)
    


@app.route('/api/get-data', methods=['GET'])
def response():
    return jsonify(response)
    
