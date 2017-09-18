# -*- coding: utf-8 -*-

import twitter
import oauth_init
import dictionary

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = dictionary.randomDictionary()
	print(status)

	f = t.statuses.update(status=status)
	print(f)

tweet()
