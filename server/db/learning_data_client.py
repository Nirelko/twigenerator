from db.mongodb_client import MongoDBClient
from configuration.configuration_managar import ConfigurationManagar

class LearningDataClient(MongoDBClient):
    def __init__(self):
        config = ConfigurationManagar.get_config()
        super().__init__(config['MONGODB']['LEARNING_DATA_URI'],
                         config['MONGODB']['LEARNING_DATA_DB_NAME'])

    # Writes the learned data to the mongodb
    def insert_learning_data(self, learning_datas):
        self.db.data.insert_many([learning_data.toJSON() for learning_data in learning_datas])

    def get_tweets_cursor(self):
        return self.db.data.find()
