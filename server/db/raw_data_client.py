from db.mongodb_client import MongoDBClient
from configuration.configuration_managar import ConfigurationManagar

class RawDataClient(MongoDBClient):
    def __init__(self):
        config = ConfigurationManagar.get_config()
        super().__init__(config['MONGODB']['RAW_DATA_URI'],
                         config['MONGODB']['RAW_DATA_DB_NAME'])

    # Returns the cursor
    def get_tweets_cursor(self, limit=1000, batch_size=10):
        collection = self.db.twitterdb
        cursor = collection.find().limit(limit)
        cursor.batch_size(batch_size)

        return cursor
