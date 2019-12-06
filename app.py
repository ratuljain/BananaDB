from flask import Flask, jsonify

from HashRing import ConsistentHashRing

app = Flask(__name__)

c = ConsistentHashRing()
c.add_node('n1')
c.add_node('n2')
c.add_node('n3')


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/get-node/<string:key>/")
def get_node_for_key(key):
    return jsonify({'node': c.find_node_for_key(key)})


@app.route("/add-node/<string:name>/")
def add_node(name):
    try:
        c.add_node(name)
    except:
        print('Already exists')

    return jsonify({'ring': c.ring})


if __name__ == "__main__":
    app.run(debug=True)
