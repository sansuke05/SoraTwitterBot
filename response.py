#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re

def random_response():
    f = open('/home/pi/projects/SoraTwitterBot/dictionary/random.txt')
    #f = open('./dictionary/random.txt')
    buffar = f.readlines()
    f.close()

    phrase = random.choice(buffar).split(',')

    # Status is a duplicate対策
    for n in range(random.randint(0,5)):
        phrase[0] += '.'

    phrase[0] = phrase[0].replace('\n','')
    return phrase

# randomDictionary()
def reply_response(swicher,text,user_name):
    f = None
    if swicher=='R':
        f = open('/home/pi/projects/SoraTwitterBot/dictionary/pattern.txt')
    else:
        f = open('/home/pi/projects/SoraTwitterBot/dictionary/pattern2.txt')

    buffar = f.readlines()
    f.close()

    # パターンマッチ
    for line in buffar:
        phrase = line.replace('\n','').split(':')
        _pattern = phrase[0]
        _responses = phrase[1].split(',')
        _response = random.choice(_responses)
        m = re.search(_pattern, text)

        if m:
            # 反応を整形
            _response = re.sub('<br>','\n',_response)
            _response = re.sub('<name>',user_name,_response)

            # Status is a duplicate対策
            for n in range(random.randint(0,3)):
                _response += '.'
            return _response

    return 'F'

