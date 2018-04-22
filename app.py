from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

movies = [
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
    print("get_data called 2")
    return jsonify({'movies': movies})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
