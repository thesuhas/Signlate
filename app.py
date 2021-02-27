from flask import Flask, jsonify, request, Response
import numpy as np
import cv2
import jsonpickle

app = Flask(__name__)

@app.route('/')
def nothing():
    return jsonify({"message": "This app translates sign language"})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})

@app.route('/test', methods=['POST'])
def fail():
    r = request
    nparr = np.fromstring(r.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")