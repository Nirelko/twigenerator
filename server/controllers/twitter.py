import tweepy
import os
from binascii import a2b_base64

class TwitterController:
    def __init__(self):
        auth = tweepy.OAuthHandler('S7j42Ae415zoWxtUARUmTvhLa', 
                                   'fPyaJVSfktga4ZaNTMESQJm4tGBfBxs52T3RCX3ZTHGoGTgYoR')
        auth.set_access_token('823414505795440641-SwpQZxcKD54xlPuUGkoEHXEY0tbk7lu', 
                              '2BgJ2oXlDtEWNFH2zwEPrqCIe5nCaHOgyWFFuj8qMhRGY')
        
        self.twitterApi = tweepy.API(auth)
    
    def tweet(self, status, image, imageName):
        imageFile = open(imageName, 'wb')
        imageFile.write(a2b_base64(image))
        imageFile.close()

        self.twitterApi.update_with_media(imageName, status=status)

        os.remove(imageName)

