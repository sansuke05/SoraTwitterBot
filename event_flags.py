# -*- coding: utf-8 -*-
# イベントコンフィグファイル管理用

import configparser
import os

# 定数
NO_EVENT_FLAG = 0
SLEEP_MANAGER_EVENT = 1

SECTION1 = 'event_flags'
FILE_PATH = "./system/setting.ini"


config = ConfigParser.ConfigParser()


# フラグ管理用設定ファイル作成
def create_setting_file(event_flag):
    config.add_section(SECTION1)
    config.set(SECTION1, 'event_flag', event_flag)

    with open(FILE_PATH, 'w', encoding='utf8') as file:
        config.write(file)
    

# 設定ファイルからフラグの読み込み
def get_event_flags():
    if os.path.exists(FILE_PATH):
        config.read(FILE_PATH, encoding='utf8')
    else:
        create_setting_file(NO_EVENT_FLAG)
        return NO_EVENT_FLAG

    return config.get(SECTION1, 'event_flag')


# 設定ファイルにフラグをセット
def set_event_flags(event_flag):
    if os.path.exists(FILE_PATH):
        config.read(FILE_PATH, encoding='utf8')
        config.set(SECTION1, 'event_flag', event_flag)

        with open(FILE_PATH, 'w', encoding='utf8') as file:
            config.write(file)
        return
    else:
        create_setting_file(event_flag)
        return