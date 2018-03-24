from pymongo import MongoClient

""" A class providing structure and access to the Database """
class MongoDBClient(object):
    # Initializing the mongodb client with the given credentials
    def __init__(self, connection_string, db_name):
        self.connection_string = connection_string
        self.db_name = db_name

        self.client = MongoClient(self.connection_string)
        self.db = self.client[db_name]
