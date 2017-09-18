# -*- coding: utf-8 -*-

import twitter
import oauth_init
import dictionary

t = twitter.Twitter(auth=oauth_init.auth)

def tweet():
	status = dictionary.randomDictionary()
	print(status)

	f = t.statuses.update(status=status)
<<<<<<< HEAD
	print(f)

tweet()
# readUserstream()
=======
>>>>>>> 57868b74290129d9245a60cd1a27ad0ad39f46ad
	print(f)

tweet()
# readUserstream()
