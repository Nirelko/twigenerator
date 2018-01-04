from tweet_generator.tweet_generator import TweetGenerator

"""
Main Class 
"""

def main():
    tweet_generator = TweetGenerator()

    tweet_generator.generate_features()


    #print('Extracted Features: %d' % len(features))
	# save to file
    # dump(features, open('features.pkl', 'a+b'))
    # dump(texts, open('texts.pkl', 'a+b'))

if __name__ == '__main__':
    main()
