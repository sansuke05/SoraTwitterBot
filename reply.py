# -*- coding: utf-8 -*-

import tweepy
import oauth_init
import datetime
import response
import event_flags
from sleep_manager import form_reply

api = tweepy.API(oauth_init.auth)

class Listener(tweepy.StreamListener):
    """docstring for Listener"""
    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)

        tweet = ''
        _response = ''
        _user_id = status.user.screen_name
        _user_name = status.user.name
        _reply_id = status.id

        # リプライに対する応答
        if str(status.in_reply_to_screen_name)=="dds_sora":

            # 特定の人からのリプかつイベントが発生していればイベントごとに処理を変更
            if event_flags.get_event_flags() == event_flags.SLEEP_MANAGER_EVENT and \
            _user_id == 'sansuke05':
                _response = form_reply.reply_sleep_manager_responce(status.text,_user_name)
            else:
                _response = response.reply_response('R',status.text,_user_name)
        elif str(_user_id)!="dds_sora":
            # TLに対する反応
            _response = response.reply_response('TL',status.text,_user_name)

        else:
            return True


        if _response=='F':
            return True
        tweet = '@'+ str(_user_id) + ' ' \
        + _response + '\n'

        try:
            api.update_status(
                status=tweet,
                in_reply_to_status_id=_reply_id)
            # api.update_with_media(
            #           status='画像付きだってできるんよ',
            #           filename='（画像ファイルパス）')
        except tweepy.TweepError as e:
            print(e.reason)
            err_rep = '@' + str(_user_id) + ' ツイートできないみたい...' \
                + '\nerror status: ' + e.reason
            api.update_status(status=err_rep)


        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True
        
listener = Listener()
stream = tweepy.Stream(oauth_init.auth, listener)
stream.userstream()