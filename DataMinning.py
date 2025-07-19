import tweepy
import pandas as pd

bearer_token = 'Token here'

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

# Funtion to extract tweets

def get_tweets(userId, number_of_tweets):

    tweets = client.get_users_tweets(id=userId, max_results=number_of_tweets)

    tweets_array=[]

    for tweet in tweets.data:
        tweets_array.append(tweet)

    #df = pd.DataFrame(tweets_array).T
    #df.to_excel()


if __name__ == '__main__':
    get_tweets(2622731, 50)