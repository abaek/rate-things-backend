from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
import pymysql

app = Flask(__name__)
CORS(app)

sample_data = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello():
    print("Hi!")
    return "Hello World!"

@app.route('/data', methods=['GET'])
def get_data():
    print("get_data called")
    return jsonify({'movies': sample_data})

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = pymysql.connect(
        db='example',
        user='root',
        passwd='hello123',
        host='localhost')
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    movies = [{"title": r[0], "rating": r[1]} for r in c.fetchall()]
    return jsonify(movies)

#    print("get_movies_called")
#    with open('movies.json', 'r') as f:
#        movies = json.load(f)
#    return jsonify(movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

