import configparser

class ConfigurationManagar(object):
    __instance = None

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    @staticmethod
    def get_config():
        if not ConfigurationManagar.__instance:
            ConfigurationManagar.__instance = ConfigurationManagar()

        return ConfigurationManagar.__instance.config