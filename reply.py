# -*- coding: utf-8 -*-

import twitter
import oauth_init
import json

t = twitter.Twitter(auth=oauth_init.auth)
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
domain = 'userstream.twitter.com'

def readUserstream():
	t_userstream = twitter.TwitterStream(auth=oauth_init.auth,domain=domain)

	for msg in twitter.userstream.user():
		print(msg)

#def getTimeline():
	#r = requests.post(url, auth=auth, stream=True, data={"track":"@"})
#	params = {
#			"count":200, #ツイートを最新から何件取得するか(最大200件)
#			"include_entities" : 1, #エンティティ(画像のURL等)をツイートに含めるか
#			"exclude_replies" : 1, #リプライを含めるか
#			}

#	req = oauth_init.auth1.get(url, params=params)

#	if req.status_code == 20:
#		timeline = json.loads(req.text)
#	
#		for tweet in timeline:
#			print(tweet["text"])
#	else:
#		print("Error: %d" % req.status_code)

readUserstream()