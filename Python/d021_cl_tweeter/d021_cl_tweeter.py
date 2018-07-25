import tweepy

# consumer_key = os.environ['TWEEPY_CONSUMER_KEY']
# consumer_secret = os.environ["TWEEPY_CONSUMER_SECRET"]
# access_token = os.environ["TWEEPY_ACCESS_TOKEN"]
# access_token_secret = os.environ["TWEEPY_ACCESS_TOKEN_SECRET"]

consumer_key = input("Input consumer key: ")
consumer_secret = input("Input consumer secret: ")
access_token = input("Input access token: ")
access_token_secret = input("Input access token secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

while True:
    tweet = input("Enter your tweet text here: ")
    if len(tweet) <= 280:
        break
    else:
        print("Your tweet was too long, try again...\n")

api.update_status(tweet)