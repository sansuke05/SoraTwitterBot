#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import oauth_init
from system import conf
 
# key
 
api = tweepy.API(oauth_init.auth1)
 
api.update_status("This is test tweet!!")
print('Done!')