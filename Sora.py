# -*- coding: utf-8 -*-

import twitter
import os
import dictionary
# from requests_oauthlib import OAuth1Session
import json
from system import conf

# url = "https://api.twitter.com/1.1/statuses/update.json"

auth = twitter.OAuth(
	consumer_key=conf.CONSUMER_KEY,
	consumer_secret=conf.CONSUMER_SECRET,
	token=conf.ACCESS_TOKEN_KEY,
	token_secret=conf.ACCESS_TOKEN_SECRET,
	)

t = twitter.Twitter(auth=auth)

def readUserstream():
	#r = requests.post(url, auth=auth, stream=True, data={"track":"@"})

	t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

	count = 0
	for msg in twitter.userstream.user():
		print(msg)
		if count > 10:
			break
		count+=1

def tweet():
	status = dictionary.randomDictionary()
	print(status)

	# params = {"status": status}
	f = t.statuses.update(status=status)
	# print(f)

tweet()
# readUserstream()