# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/pi/projects/SoraTwitterBot/')
import oauth_init
import event_flags
import tweepy

api = tweepy.API(oauth_init.auth)
responce_counter = 0

def reply_introduction():
    event_flags.set_event_flags(event_flags.SLEEP_MANAGER_EVENT)

    reply_name = '@sansuke05'
    status = reply_name + ' マスター、昨日の睡眠時間の記録するよ〜\nまず、就寝時間を教えてね..'

    print(status)

    r = api.update_status(status=status)
    #print(r)


def reply_sleep_manager_responce(text,user_name):
    global responce_counter 
    responce_counter += 1
    print(responce_counter)

    #debug
    return 'SUCCESS'



if __name__ == '__main__':
    reply_introduction()