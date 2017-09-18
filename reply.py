# -*- coding: utf-8 -*-

import twitter
import oauth_init

t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

def readUserstream():
	#r = requests.post(url, auth=auth, stream=True, data={"track":"@"})

	count = 0
	for msg in twitter.userstream.user():
		print(msg)
		if count > 10:
			break
		count+=1