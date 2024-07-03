import tweepy
from textblob import TextBlob

consumer_key='wU9DxoEAxQpILXjFy78gJ0SX2'
consumer_secret='pcjzKL2dLE9AmXyD9iHjqS0BzpviptpvzlubsM1J4BNxQDoNYw'

access_token='1313787586108772354-MBoVnQ2nLpK1U7uej8aSV0ZOdhXVya'
access_token_secret='5hw5ma3cef64Rpou54MXN2E3Vzm1cEIw8DsZRNUNWFg7f'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets = api.search_tweets('Trump')
for tweet in public_tweets:
    print(tweet.text)
    analysis= TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")