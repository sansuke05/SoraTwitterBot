# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.getcwd())
import oauth_init

import twitter
import dictionary

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = 'おやすみなさ〜い！..'
	print(status)

	f = t.statuses.update(status=status)
	print(f)

tweet()
