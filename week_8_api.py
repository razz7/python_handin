from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql
from flask_json import json_response

#from flask_mysqldb import MySQL


app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/netflix'


db = mysql.connect(
    host = "db", # would be localhost if not running in docker
    user = "root",
    passwd = "root",
    db = "netflix"
)


@app.route('/api/get-data', methods=['GET'])
def response():
    res = []
    cur = db.cursor()
    query = 'select * from netflix where release_year = 2000'
    cur.execute(query)
    result = cur.fetchall()
    for m in result:
        res.append(m)
    return jsonify(res)


@app.route('/api/all', methods=['GET'])
def all():
    resall = []
    cur = db.cursor()
    q = 'select * from netflix'
    cur.execute(q)
    qres = cur.fetchall()
    for m in qres:
        resall.append(m)
    return jsonify(resall)

