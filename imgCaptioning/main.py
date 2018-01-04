from tweet_generator.tweet_generator import TweetGenerator

"""
Main Class 
"""

def main():
    # Create tweet generator instance
    tweet_generator = TweetGenerator()

    # Generates the features for the tweets and save them to the mongodb
    #tweet_generator.generate_features()
    tweet_generator.pre_process_data()

if __name__ == '__main__':
    main()
