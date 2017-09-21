# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/pi/projects/SoraTwitterBot/')
import oauth_init
from datetime import datetime
import twitter

t = twitter.Twitter(auth=oauth_init.auth)
h = datetime.now().hour

def tweet():
	status = ''
	if h == 8:
		status = 'おはようございます〜！'
	else:
		status = 'おやすみなさ〜い！..'

	print(status)

	f = t.statuses.update(status=status)
	#print(f)

tweet()
