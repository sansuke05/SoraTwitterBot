# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/pi/projects/SoraTwitterBot/')
import oauth_init
from datetime import datetime
import tweepy

api = tweepy.API(oauth_init.auth)
h = datetime.now().hour

def tweet():
    status = ''
    if h == 8:
        status = 'おはようございます〜！'
    elif h == 12:
        status = 'お昼だよ！'
    else:
        status = 'おやすみなさ〜い！'

    print(status)

    r = api.update_status(status=status)
    #print(r)

tweet()
