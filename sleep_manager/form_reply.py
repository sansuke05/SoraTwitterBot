# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/pi/projects/SoraTwitterBot/')
import oauth_init
import event_flags
from datetime import datetime, date
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy

ERROR = 0
CSV_PATH = "./csv/timedata.csv"

api = tweepy.API(oauth_init.auth)
responce_counter = 0

# 日付を作成
today = date.today()
yesterday = today - datetime.timedelta(days=1)
str_yesterday = str(yesterday.month) + '月' + str(yesterday.day) + '日'


def reply_introduction():
    event_flags.set_event_flags(event_flags.SLEEP_MANAGER_EVENT)

    reply_name = '@sansuke05'

    status = reply_name + ' マスター、' + str_yesterday + \
    'の睡眠時間の記録するよ〜\nまず、就寝時間を教えてね'

    print(status)

    r = api.update_status(status=status)
    #print(r)


def reply_sleep_manager_responce(text,user_name):
    global responce_counter
    sleep_time = datetime.now()
    waikup_time = datetime.now()
    next_responce = 'error occured!'

    responce_counter += 1
    print(responce_counter)

    time = get_time(text)

    if not time[0]:
        return time[1]

    #時間を整形
    if len(time[0]) == 1:
        time[0] = '0' + time[0]
    if len(time[1]) == 1:
        time[1] = '0' + time[1]


    if responce_counter == 1: # 就寝時間
        str_time = time[0] + ':' + time[1] + ':00'
        sleep_time = datetime.strptime(str_time, '%H:%M:%S')
        sleep_time = sleep_time.time()
        next_responce = '起床時間を教えてね'

    elif responce_counter == 2: #起床時間
        str_time = time[0] + ':' + time[1] + ':00'
        waikup_time = datetime.strptime(str_time, '%H:%M:%S')
        waikup_time = waikup_time.time()
        next_responce = '記録したよ〜！\n' + str_yesterday + 'までの記録を送るね！'

        # csvに時間を記録
        write_csv(sleep_time, waikup_time)

    return next_responce


# テキストから時間を抽出
def get_time(text):
    m = re.findall('[\d]+', text)
    if len(m) == 2:
        return m;

    return [ERROR,'何時かわかんないよ〜\nもう一度入力し直してね']


# csvファイルに時間を記録
def write_csv(sleep_time, waikup_time):
    
    if not os.path.exists(CSV_PATH):
        # データフレームを作成
        df = pd.DataFrame(
            [[today, sleep_time, waikup_time]],
            columns=['記録日', '就寝時間', '起床時間']
            )
        df.to_csv(CSV_PATH, index=False, encoding="utf-8")
    else:
        w = pd.DataFrame([[today, sleep_time, waikup_time]])
        w.to_csv(CSV_PATH, index=False, encoding="utf-8", mode='a', header=False)


# グラフイメージをプロット
def plot_graph():
    plt = 


if __name__ == '__main__':
    reply_introduction()