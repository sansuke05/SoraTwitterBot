# -*- coding: utf-8 -*-

import twitter
import tweepy
# from requests_oauthlib import OAuth1Session
from system import conf

# url = "https://api.twitter.com/1.1/statuses/update.json"

auth = twitter.OAuth(
	consumer_key=conf.CONSUMER_KEY,
	consumer_secret=conf.CONSUMER_SECRET,
	token=conf.ACCESS_TOKEN_KEY,
	token_secret=conf.ACCESS_TOKEN_SECRET,
	)

auth1 = tweepy.OAuthHandler(conf.CONSUMER_KEY, conf.CONSUMER_SECRET)
auth1.set_access_token(conf.ACCESS_TOKEN_KEY, conf.ACCESS_TOKEN_SECRET)