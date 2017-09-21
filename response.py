#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re

def random_response():
	f = open('/home/pi/projects/SoraTwitterBot/dictionary/random.txt')
	#f = open('./dictionary/random.txt')
	buffar = f.readlines()
	f.close()

	phrase = random.choice(buffar)

	# Status is a duplicate対策
	for n in range(random.randint(1,5)):
		phrase += '.'

	return phrase.replace('\n','')

# randomDictionary()
def reply_response(reply,user_name):
	f = open('/home/pi/projects/SoraTwitterBot/dictionary/pattern.txt')

	buffar = f.readlines()
	f.close()

	# パターンマッチ
	for line in buffar:
		phrase = line.replace('\n','').split(':')
		_pattern = phrase[0]
		_responce = phrase[1]
		m = re.search(_pattern, reply)

		if m:
			# 反応を整形
			_responce = re.sub('<br>','\n',_responce)
			_responce = re.sub('<name>',user_name,_responce)

			# Status is a duplicate対策
			for n in range(random.randint(1,3)):
				_responce += '.'
			return _responce

	return 'F'
