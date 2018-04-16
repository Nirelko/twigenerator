from flask import Flask, request
from controllers.generator import GeneratorController
from controllers.twitter import TwitterController

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] ='./uploads'

generatorController = GeneratorController()
twitterController = TwitterController()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/twit/generator', methods=['POST'])
def generate_tweet():
    return generatorController.generate_tweet(request.files)

@app.route('/api/twitter/tweet', methods=['POST'])
def post_tweet():
    return twitterController.tweet(request.form['status'], request.form['image'], request.form['imageName'])

if __name__ == '__main__':
    app.run(debug=True)