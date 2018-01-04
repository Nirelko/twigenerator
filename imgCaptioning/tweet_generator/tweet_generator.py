import urllib
import cv2
import numpy as np
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image as keras_image
from keras.applications.inception_v3 import preprocess_input

from models.learning_data import LearningData
from db.db_context import DBContext

class TweetGenerator:
    def generate_features(self):
        model = InceptionV3(weights='imagenet', include_top=False, pooling='avg')
        tweets = DBContext.get_raw_data_client().get_tweets_cursor(100, 10)
        learning_datas = []
        current_retrieved = tweets.retrieved

        for tweet in tweets:
            img = self.url_to_image(tweet['img'])

            if isinstance(img, (list, tuple, np.ndarray)):
                img_preprocessed = self.preprocess_image(img)
                pred = model.predict(img_preprocessed)

                print(tweet['_id'])
                print(tweets.retrieved)

                learning_datas.append(LearningData(tweet['_id'], tweet['text'], pred))

            if current_retrieved != tweets.retrieved:
                DBContext.get_learning_data_client().insert_learning_data(learning_datas)
                learning_datas = []
                current_retrieved = tweets.retrieved

    def url_to_image(self, url, resize=299):
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

    def preprocess_image(self, image):
        """
        preporcess the image as needed for InceptionV3
        """

        img_preprocessed = keras_image.img_to_array(image)
        img_preprocessed = np.expand_dims(img_preprocessed, axis=0)
        img_preprocessed = preprocess_input(img_preprocessed)

        return img_preprocessed