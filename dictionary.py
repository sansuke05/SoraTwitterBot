#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def randomDictionary():
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
