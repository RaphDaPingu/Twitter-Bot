import tweepy
import time
import random
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
   
def tweet():
    lines = open("nouns.txt").read().splitlines()
    random_line = random.choice(lines)

    num = random.randint(0, 1)
    tweet_str = "Lisa the "

    if (num == 0):
        tweet_str += random_line + "ful"

    else:
        tweet_str += random_line + "less"
    
    api.update_status(tweet_str)

tweet()
