from flask import Flask, jsonify, request
from controllers.generator import GeneratorController

app = Flask(__name__, static_url_path='/static')

generatorController = GeneratorController()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/generator')
def generate_tweet():
    return jsonify(generatorController.generate(request.args.get('image', '')))

if __name__ == '__main__':
    app.run(debug=True)