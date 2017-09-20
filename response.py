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
def reply_response(reply):
	f = open('/home/pi/projects/SoraTwitterBot/dictionary/pattern.txt')

	buffar = f.readlines()
	f.close()

	# パターンマッチ
	for line in buffar:
		phrase = line.replace('\n','').split(':')
		pattern = phrase[0]
		m = re.search(pattern, reply)

		if m:
			return phrase[1]

	return 'F'
