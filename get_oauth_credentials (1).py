# Taken from https://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html

import tweepy

consumer_token = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Unable to get the redirect URL")
