import configparser

class ConfigurationManagar(object):
    __instance = None

    def __init__(self):
        # Setting the config file and parse it
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    # Returns the singleton config
    @staticmethod
    def get_config():
        # Check if the config has been created and creates it if not
        if not ConfigurationManagar.__instance:
            ConfigurationManagar.__instance = ConfigurationManagar()

        return ConfigurationManagar.__instance.config