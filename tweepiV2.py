import tweepy
import xlsxwriter
bearer_token = 'barrer_token'

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

# Funtion to extract tweets

def get_action(userId, number_limit, action):

    results_array=[]

    match action:

        case 1:
            tweets = client.get_users_tweets(id=userId, max_results=number_limit)

            for tweet in tweets.data:
                results_array.append(str(tweet))

        case 2:
            mentions = client.get_users_mentions(id=userId, max_results=number_limit)

            for mention in mentions.data:
                results_array.append(str(mention))
        
        case 3:
            followers = client.get_users_followers(id=userId, max_results=number_limit)

            print(followers)

            for follower in followers.data:
                results_array.append(str(follower))
    

    print(results_array)

    workbook = xlsxwriter.Workbook('x_results.xlsx')
    worksheet = workbook.add_worksheet()

    for row, data in enumerate(results_array):
        worksheet.write(row, 0, data)

    workbook.close()


if __name__ == '__main__':
    userId = input(f'Enter the userID: ')
    action = input(f'Enter the action: ')


    get_action(int(userId), 50, int(action))