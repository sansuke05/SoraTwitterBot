# -*- coding: utf-8 -*-

import tweepy
import oauth_init
import datetime
import response

api = tweepy.API(oauth_init.auth1)

class Listener(tweepy.StreamListener):
	"""docstring for Listener"""
	def on_status(self, status):
		status.created_at += datetime.timedelta(hours=9)

		# リプライに対する応答
		if str(status.in_reply_to_screen_name)=="dds_sora":
			_user = status.user.screen_name
			_response = response.reply_response(status.text,_user)
			if _response=='F':
				return True
			tweet = '@'+ str(_user) + ' ' \
			+ _response + '\n'
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