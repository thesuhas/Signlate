from flask import Flask, jsonify, request, Response
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def nothing():
    return jsonify({"message": "This app translates sign language"})

#GET methods (functioning properly)
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})

#POST methods (Not being accepted)
@app.route('/upload', methods=['POST'])
def fail():
    file_img = request.files['file']
    print(file_img)
    img = request.files['file'].read()
    img = Image.open(io.BytesIO(img))
    # Converting image to np array
    img2 = np.array(img)

    return jsonify({"test": "received"})
