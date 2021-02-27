from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def nothing():
    return jsonify({"message": "This app translates sign language"})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})

@app.route('/test', methods=['POST'])
def test():
    return jsonify({'test': 'works you fool'})