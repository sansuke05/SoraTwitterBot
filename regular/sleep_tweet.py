# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.pardir)
import oauth_init

import twitter
import oauth_init
import dictionary

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = 'おやすみなさ〜い！'
	print(status)

	f = t.statuses.update(status=status)
	print(f)

tweet()
