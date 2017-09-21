# -*- coding: utf-8 -*-

import twitter
import oauth_init
import response
import sys

t = twitter.Twitter(auth=oauth_init.auth)
argvs = sys.argv
args = len(argvs)

def tweet():
	status = response.random_response()
	print(status)
	print(argvs)

	if argvs[1] == 'restart':
		status = 'Reconnected to userstream successfully!'

	f = t.statuses.update(status=status)
	print(f)

tweet()
