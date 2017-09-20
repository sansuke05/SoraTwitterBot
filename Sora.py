# -*- coding: utf-8 -*-

import twitter
import oauth_init
import responce

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = responce.randomResponce()
	print(status)

	f = t.statuses.update(status=status)
	print(f)

tweet()
