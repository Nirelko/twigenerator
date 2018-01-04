from configuration.configuration_managar import ConfigurationManagar
from db.mongodb_client import MongoDBClient


class DBContext(object):
    __instance = None

    def __init__(self):
        config = ConfigurationManagar.get_config()

        # Setting the tweets mongo client
        self.raw_data_client = MongoDBClient(config['MONGODB']['RAW_DATA_URI'],
                                             config['MONGODB']['RAW_DATA_DB_NAME'])

        # Setting the learning data mongo client
        self.learning_data_client = MongoDBClient(config['MONGODB']['LEARNING_DATA_URI'],
                                                  config['MONGODB']['LEARNING_DATA_DB_NAME'])

    @staticmethod
    def get_instance():
        if not DBContext.__instance:
            DBContext.__instance = DBContext()

        return DBContext.__instance

    @staticmethod
    def get_raw_data_client():
        return DBContext.get_instance().raw_data_client

    @staticmethod
    def get_learning_data_client():
        return DBContext.get_instance().learning_data_client
