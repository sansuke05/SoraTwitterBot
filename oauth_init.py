# -*- coding: utf-8 -*-

import twitter
import tweepy
# from requests_oauthlib import OauthSession
from system import conf

# url = "https://api.twitter.com/1.1/statuses/update.json"

auth = tweepy.OAuthHandler(conf.CONSUMER_KEY, conf.CONSUMER_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN_KEY, conf.ACCESS_TOKEN_SECRET)