#!/bin/bash
# プロセス監視用シェル
pid=$(cat /home/pi/projects/SoraTwitterBot/reply_py.pid)
proc=$(ps aux | grep python)

if [[ !($proc =~ $pid) ]]; then
 	# プロセス再起動
 	sh /home/pi/projects/SoraTwitterBot/reply_process.sh
 	# プロセス再起動をTwitterに通知
 	~/.pyenv/versions/3.6.1/bin/python /home/pi/projects/SoraTwitterBot/Sora.py restart
fi