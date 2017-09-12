# -*- coding: utf-8 -*-

import twitter
import os
import dictionary
# from requests_oauthlib import OAuth1Session
import json

CONSUMER_KEY = 'A9jhPjQxwCZEz1LmYcMMTBccD'
CONSUMER_SECRET = '0xmmFZ2fQjqju1VYb05x1dUWYHRNVPb7VLChWElpS34gvVKGfW'
ACCESS_TOKEN_KEY = '832506075068784640-H5XvBBSL7R87pyoloCsXIPMmQN1gGIf'
ACCESS_TOKEN_SECRET = '0gJRodRKNSJ4kGSOtR7dWETnGXcxjBKXZYxYQkTgh02db'

# url = "https://api.twitter.com/1.1/statuses/update.json"

auth = twitter.OAuth(
	consumer_key=os.environ["CONSUMER_KEY"],
	consumer_secret=os.environ["CONSUMER_SECRET"],
	token=os.environ["ACCESS_TOKEN_KEY"],
	token_secret=os.environ["ACCESS_TOKEN_SECRET"],
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
	print(f)

tweet()
# readUserstream()