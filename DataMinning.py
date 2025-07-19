import tweepy
import xlsxwriter
bearer_token = 'Bearer_token Here'

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

# Funtion to extract tweets

def get_tweets(userId, number_of_tweets):

    tweets = client.get_users_tweets(id=userId, max_results=number_of_tweets)

    tweets_array=[]

    for tweet in tweets.data:
        tweets_array.append(str(tweet))

    print(tweets_array)

    workbook = xlsxwriter.Workbook('tweets.xlsx')
    worksheet = workbook.add_worksheet()

    for row, data in enumerate(tweets_array):
        worksheet.write(row, 0, data)

    workbook.close()


if __name__ == '__main__':
    get_tweets(2622731, 5)