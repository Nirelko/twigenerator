from pymongo import MongoClient

""" A class providing structure and access to the Database """
class MongoDBClient(object):
    def __init__(self, connection_string, db_name):
        self.connection_string = connection_string
        self.db_name = db_name

        self.client = MongoClient(self.connection_string)
        self.db = self.client[db_name]

    def get_tweets_cursor(self, limit=1000, batch_size=10):
        collection = self.db.twitterdb
        cursor = collection.find().limit(limit)
        cursor.batch_size(batch_size)

        return cursor

    def insert_learning_data(self, learning_datas):
        self.db.data.insert_many([learning_data.toJSON() for learning_data in learning_datas])
