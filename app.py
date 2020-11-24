from flask import Flask, request, jsonify
from flask import json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Test

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = "development"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand) # init migrate upgrade downgrade


@app.route('/')
def main():
    return "Hola desde Flask"


@app.route('/api/tests', methods=['GET', 'POST'])
@app.route('/api/tests/<id>', methods=['GET', 'PUT', 'DELETE'])
def tests(id = None):
    if request.method == 'GET':
        if id is not None:
            test = Test.query.get(id)
            if test:
                return jsonify(test.serialize()), 200
            else:
                return jsonify({"error": "Test doesn't exist"}), 404
        else:
            tests = Test.query.all()
            tests = list(map(lambda test: test.serialize(), tests))
            return jsonify(tests), 200

    if request.method == 'POST':
        name = request.json.get("name")
        email = request.json.get("email")
        phone = request.json.get("phone")

        test = Test()
        test.name = name
        test.email = email
        test.phone = phone

        test.save()

        return jsonify(test.serialize()), 201

    if request.method == 'PUT':
        name = request.json.get("name")
        email = request.json.get("email")
        phone = request.json.get("phone")

        test = Test.query.get(id)
        test.name = name
        test.email = email
        test.phone = phone

        test.update()

        return jsonify(test.serialize()), 200

    if request.method == 'DELETE':
        name = request.json.get("name")
        email = request.json.get("email")
        phone = request.json.get("phone")

        test = Test.query.get(id)
        test.name = name
        test.email = email
        test.phone = phone

        test.delete()

        return jsonify(test.serialize()), 200


""" 
@app.route('/api/test', methods=['GET'])
def by_get():
    return "llegando por el metodo GET"

@app.route('/api/test', methods=['POST'])
def by_post():
    return "llegando por el metodo POST"

@app.route('/api/test', methods=['PUT'])
def by_put():
    return "llegando por el metodo PUT"

@app.route('/api/test', methods=['DELETE'])
def by_delete():
    return "llegando por el metodo DELETE" 
"""
""" 
@app.route('/api/test/<name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all_methods(name):
    if request.method == 'GET':
        return "{} estas llegando por el metodo GET".format(name, lastname)
    if request.method == 'POST':
        return "{} estas llegando por el metodo POST".format(name)
    if request.method == 'PUT':
        return "{} estas llegando por el metodo PUT".format(name)
    if request.method == 'DELETE':
        return "{} estas llegando por el metodo DELETE".format(name)
 """
""" 
@app.route('/api/test/<name>', methods=['GET', 'PUT'])
def get_put_methods(name):
    if request.method == 'GET':
        return "{} estas llegando por el metodo GET".format(name)
    if request.method == 'PUT':
        return "{} estas llegando por el metodo PUT".format(name)

@app.route('/api/test', methods=['POST', 'DELETE'])
def post_delete_methods():
    if request.method == 'POST':
        return "estas llegando por el metodo POST"
    if request.method == 'DELETE':
        return "estas llegando por el metodo DELETE"
"""
""" 
@app.route('/api/test', methods=['GET', 'POST'])
@app.route('/api/test/<name>', methods=['GET', 'PUT', 'DELETE'])
def all_methods_together(name = None):
    if request.method == 'GET':
        msg = "{} estas llegando por el metodo GET".format(name)
        return jsonify({"msg": msg}), 200
    if request.method == 'POST':
        fullname = request.json.get("fullname")
        age = request.json.get("age")
        msg = "{} ({}) estas llegando por el metodo POST".format(fullname, age)
        return jsonify({"msg": msg}), 301 
    if request.method == 'PUT':
        msg = "{} estas llegando por el metodo PUT".format(name)
        return jsonify({"msg": msg}), 500 
    if request.method == 'DELETE':
        msg = "{} estas llegando por el metodo DELETE".format(name)
        return jsonify({"msg": msg}), 404
"""




if __name__ == '__main__':
    manager.run()