# -*- coding: utf-8 -*-

import tweepy
import oauth_init
import datetime

api = tweepy.API(oauth_init.auth1)

class Listener(tweepy.StreamListener):
	"""docstring for Listener"""
	def on_status(self, status):
		status.created_at += datetime.timedelta(hours=9)

		# 返信
		if str(status.in_reply_to_screen_name)=="dds_sora":
			tweet = '@'+ str(status.user.screen_name) + ' ' + 'こんにちは！\n' \
			+ str(datetime.datetime.today())
			api.update_status(status=tweet)
		return True

	def on_error(self, status_code):
		print('Got an error with status code: ' + str(status_code))
		return True

	def on_timeout(self):
		print('Timeout...')
		return True
		
listener = Listener()
stream = tweepy.Stream(oauth_init.auth1, listener)
stream.userstream()
#readUserstream()