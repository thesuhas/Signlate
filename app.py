from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def nothing():
    return jsonify({"message": "This app translates sign language"})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})