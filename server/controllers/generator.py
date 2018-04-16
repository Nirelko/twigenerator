import time
import random
from flask_api import status
from flask import jsonify

class GeneratorController:
    def generate_tweet(self, files):
        if 'file' not in files:
            return {'Bad Request': 'Excpected To File Request'}, status.HTTP_400_BAD_REQUEST

        file = files['file']

        if file.filename == '':
            return {'Bad File': 'No File Was Selected'}, status.HTTP_404_NOT_FOUND
        
        time.sleep(1)
        
        return jsonify({'sentence': random.randint(0,100000)})