
"""
Main Class 
"""
import configparser
import urllib
import numpy as np
import h5py as h5py
import cv2
from mongodb_client import MongoDBClient
from models.learning_data import LearningData
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image as keras_image
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import decode_predictions
from pickle import dump

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    rawDataClient = MongoDBClient(config['MONGODB']['RAW_DATA_URI'], config['MONGODB']['RAW_DATA_DB_NAME'])
    learningDataClient = MongoDBClient(config['MONGODB']['LEARNING_DATA_URI'], config['MONGODB']['LEARNING_DATA_DB_NAME'])

    tweets = rawDataClient.get_tweets_cursor(100, 10)
    model = InceptionV3(weights='imagenet', include_top=False, pooling='avg')
    learning_datas = []
    currentRetrieved = tweets.retrieved

    for tweet in tweets:
        img = url_to_image(tweet['img'])

        if isinstance(img, (list, tuple, np.ndarray)):
            img_preprocessed = preprocess_image(img)
            pred = model.predict(img_preprocessed)

            print(tweet['_id'])
            print(tweets.retrieved)

            learning_datas.append(LearningData(tweet['_id'], tweet['text'], pred))

        if currentRetrieved != tweets.retrieved:
            #dump(features, open('features.pkl', 'a+b'))
            #dump(texts, open('texts.pkl', 'a+b'))
            learningDataClient.insert_learning_data(learning_datas)
            learning_datas = []
            currentRetrieved = tweets.retrieved



    #print('Extracted Features: %d' % len(features))
	# save to file
    # dump(features, open('features.pkl', 'a+b'))
    # dump(texts, open('texts.pkl', 'a+b'))

def url_to_image(url, resize=299):
    """
    downloads an image from url, converts to numpy array,
    resizes, and returns it
    """
    try:
        response = urllib.request.urlopen(url)
        img = np.asarray(bytearray(response.read()), dtype=np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (resize, resize), interpolation=cv2.INTER_CUBIC)
    except:
        img = None
    return img

def preprocess_image(image):
    """
    preporcess the image as needed for InceptionV3
    """

    img_preprocessed = keras_image.img_to_array(image)
    img_preprocessed = np.expand_dims(img_preprocessed, axis=0)
    img_preprocessed = preprocess_input(img_preprocessed)
    return img_preprocessed

if __name__ == '__main__':
    main()
