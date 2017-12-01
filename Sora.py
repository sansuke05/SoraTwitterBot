# -*- coding: utf-8 -*-

import tweepy
import oauth_init
import response
import sys
import re

IMG_DIR = '/home/pi/projects/SoraTwitterBotgit/image/'

api = tweepy.API(oauth_init.auth)
argvs = sys.argv
args = len(argvs)

def tweet():
    statuses = []
    print(argvs)

    if 'restart' in argvs:
        # ストリーム再接続時のみ実行
        print('starting reply!')
        statuses[0] = 'Reconnected to userstream successfully!'
    else:
        statuses = response.random_response()

    print(statuses)

    if len(statuses) == 2:
        filename = IMG_DIR + statuses[1] + '.jpg'
        print(filename)
        api.update_with_media(
            status=statuses[0],
            filename=filename,
            )
        print('Done!')
    else:
        r = api.update_status(status=statuses[0])
        print(r)

if __name__ == '__main__':
    tweet()
