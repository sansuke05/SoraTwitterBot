#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import oauth_init
from system import conf
 
# key
 
api = tweepy.API(oauth_init.auth)
file_path = './image/test.jpg'
 
api.update_with_media(
    status="This is test tweet!!..",
    filename=file_path,
    )
print('Done!')