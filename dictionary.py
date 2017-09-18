#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def randomDictionary():
	f = open('/home/pi/projects/SoraTwitterBot/dictionary/random.txt')
	buffar = f.readlines()
	f.close()

	phrase = random.choice(buffar)

	return phrase.replace('\n','')

# randomDictionary()