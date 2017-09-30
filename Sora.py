# -*- coding: utf-8 -*-

import tweepy
import oauth_init
import response
import sys

api = tweepy.API(oauth_init.auth)
argvs = sys.argv
args = len(argvs)

def tweet():
    status = response.random_response()
    print(argvs)

    if 'restart' in argvs:
        print('starting reply!')
        status = 'Reconnected to userstream successfully!'

    print(status)
    f = api.update_status(status=status)
    print(f)

if __name__ == '__main__':
    tweet()
