from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import pymysql

app = Flask(__name__)
CORS(app)

def establish_conn():
    return pymysql.connect(
        db='example',
        user='root',
        passwd='hello123',
        host='localhost')

@app.route("/")
def hello():
    print("Hi!")
    return "Hello World!"

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = establish_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    movies = [{"title": r[0], "rating": r[1]} for r in c.fetchall()]
    return jsonify(movies)

@app.route('/add_movie', methods=['POST'])
def add_movie(): 
    data = request.get_json()
    title = data['title']
    rating = int(data['rating'])

    conn = establish_conn()
    c = conn.cursor()
    c.execute("INSERT INTO movies VALUES ('{}', {})".format(title.replace("'", "''"), rating))
    conn.commit()
    return "Success adding {}".format(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

