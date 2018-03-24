import urllib
import cv2
import numpy as np
from keras.utils import to_categorical
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image as keras_image, text, sequence
from keras.applications.inception_v3 import preprocess_input
from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from keras.layers import Dropout
from keras.layers.merge import add
from keras.callbacks import ModelCheckpoint

from models.learning_data import LearningData
from db.db_context import DBContext


class TweetGenerator:
    def __init__(self):
        self.max_length = 280

    # Transform the raw data from the mongodb to the learning model features
    def generate_features(self):
        # Setting the model
        model = InceptionV3(weights='imagenet', include_top=False, pooling='avg')

        # Getting the tweets fro the mongodb
        tweets = DBContext.get_raw_data_client().get_tweets_cursor(10000, 100)
        print('nirel got the data from the mongodb')
        learning_datas = []

        # The amount of tweets that has been read so far
        current_retrieved = tweets.retrieved

        # Scanning all the tweets, getting the features for each tweets and writing the learned data to the DB.
        for tweet in tweets:
            # Changing the image from url to image vector
            img = self.url_to_image(tweet['img'])

            # Check if the image parse has succeeded
            if isinstance(img, (list, tuple, np.ndarray)):
                # Preprocess the image for the model to work with it
                img_preprocessed = self.preprocess_image(img)

                # Predict the features by the model
                pred = model.predict(img_preprocessed)

                print(tweet['_id'])
                print(tweets.retrieved)

                # Appending the learned data array with the current image
                learning_datas.append(LearningData(tweet['_id'], tweet['text'], pred))

            if current_retrieved != tweets.retrieved:
                # Writing the learned data to the DB
                DBContext.get_learning_data_client().insert_learning_data(learning_datas)

                # Clearing the learned data array
                learning_datas = []
                current_retrieved = tweets.retrieved

    # Gets url of an image and transforms it to vector
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

    def pre_process_data(self):
        print("WE strated")
        learning_data = list(DBContext.get_learning_data_client().get_tweets_cursor().limit(100))
        train_data = learning_data[: round(len(learning_data) * 0.8)]
        test_data = learning_data[len(train_data):]

        train_data_dict = {data['_id']: LearningData(data['_id'],
                                                        data['text'],
                                                        data['pred']) for data in train_data}

        test_data_dict = {data['_id']: LearningData(data['_id'],
                                                        data['text'],
                                                        data['pred']) for data in test_data}

        train_tokenizer = text.Tokenizer(num_words=None,
                                   lower=True,
                                   char_level=True)

        testFilteredTexts = [train_text.lower() for train_text in self.get_all_senteces(test_data_dict)]

        train_tokenizer.fit_on_texts(self.get_all_senteces(train_data_dict))
        print(train_tokenizer.word_counts)
        self.vocab_size = len(train_tokenizer.word_index) + 1
        X1train, X2train, Ytrain = self.create_sequences(train_tokenizer, 280, train_data_dict)

        # define the model
        print('yala hitchalno')
        model = self.define_model(self.vocab_size, self.max_length)
        # define checkpoint callback
        filepath = 'model-ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5'
        checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

        # prepare sequences
        X1test, X2test, ytest = self.create_sequences(train_tokenizer, self.max_length, test_data_dict)

        # fit model
        model.fit([X1train, X2train], Ytrain, epochs=20, verbose=2, callbacks=[checkpoint],
                  validation_data=([X1test, X2test], ytest))

    def get_all_senteces(self, learning_data_dict):
        all_sentences = list()
        for key in learning_data_dict.keys():
            all_sentences.append('startseq ' + learning_data_dict[key].text + ' endseq')
        return all_sentences

    def create_sequences(self, tokenizer, max_length, learning_data):
        X1, X2, y = list(), list(), list()
        # walk through each image identifier
        for id, data in learning_data.items():
            # encode the sequence
            seq = tokenizer.texts_to_sequences([data.text])[0]
            # split one sequence into multiple X,y pairs
            for i in range(1, len(seq)):
                # split into input and output pair
                in_seq, out_seq = seq[:i], seq[i]
                # pad input sequence
                in_seq = sequence.pad_sequences([in_seq], maxlen=max_length)[0]
                # encode output sequence
                out_seq = to_categorical([out_seq], num_classes=self.vocab_size)[0]
                # store
                X1.append(data.pred[0])
                X2.append(in_seq)
                y.append(out_seq)

        return np.array(X1), np.array(X2), np.array(y)

    def define_model(self, vocab_size, max_length):
        # feature extractor model
        inputs1 = Input(shape=(2048,))
        fe1 = Dropout(0.5)(inputs1)
        fe2 = Dense(256, activation='relu')(fe1)
        # sequence model
        inputs2 = Input(shape=(max_length,))
        se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
        se2 = Dropout(0.5)(se1)
        se3 = LSTM(256)(se2)
        # decoder model
        decoder1 = add([fe2, se3])
        decoder2 = Dense(256, activation='relu')(decoder1)
        outputs = Dense(vocab_size, activation='softmax')(decoder2)
        # tie it together [image, seq] [word]
        model = Model(inputs=[inputs1, inputs2], outputs=outputs)
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        # summarize model
        return model
