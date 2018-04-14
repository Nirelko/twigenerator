import time
from flask import Flask, jsonify, request
from flask_api import status
from controllers.generator import GeneratorController
import random

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] ='./uploads'

generatorController = GeneratorController()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/twit/generator', methods=['POST'])
def generate_tweet():
    if 'file' not in request.files:
        return {'Bad Request': 'Excpected To File Request'}, status.HTTP_400_BAD_REQUEST

    file = request.files['file']

    if file.filename == '':
        return {'Bad File': 'No File Was Selected'}, status.HTTP_404_NOT_FOUND
    
    time.sleep(1)
    
    return jsonify({'sentence': random.randint(0,100000)})

if __name__ == '__main__':
    app.run(debug=True)