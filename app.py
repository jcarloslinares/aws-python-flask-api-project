from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return jsonify(message='OK!')


@app.route("/hello")
def hello():
    return make_response(jsonify(message='Hello from path!'), 201)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
