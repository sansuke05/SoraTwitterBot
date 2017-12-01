# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/pi/projects/SoraTwitterBot/')
import oauth_init
import tweepy

api = tweepy.API(oauth_init.auth)

def reply_introduction():
    reply_name = '@sansuke05'
    status = reply_name + ' マスター、昨日の睡眠時間の記録するよ〜\nまず、就寝時間を教えてね'

    r = api.update_status(status=status)
    print(r)


if __name__ == '__main__':
    reply_introduction()