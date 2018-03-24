from configuration.configuration_managar import ConfigurationManagar
from db.learning_data_client import LearningDataClient
from db.raw_data_client import RawDataClient


class DBContext(object):
    __instance = None

    def __init__(self):
        # Gets the configuration
        config = ConfigurationManagar.get_config()

        # Setting the tweets mongo client
        self.raw_data_client = RawDataClient()

        # Setting the learning data mongo client
        self.learning_data_client = LearningDataClient()

    # Get the db context singleton instance
    @staticmethod
    def get_instance():
        # Check if the instance has been created and creates it if not
        if not DBContext.__instance:
            DBContext.__instance = DBContext()

        return DBContext.__instance

    # Get the raw data mongodb client
    @staticmethod
    def get_raw_data_client():
        return DBContext.get_instance().raw_data_client

    # Get the learning data mongodb client
    @staticmethod
    def get_learning_data_client():
        return DBContext.get_instance().learning_data_client
