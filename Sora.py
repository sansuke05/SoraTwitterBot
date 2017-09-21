# -*- coding: utf-8 -*-

import twitter
import oauth_init
import response

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = response.random_response()
	print(status)

	f = t.statuses.update(status=status)
	#print(f)

tweet()
