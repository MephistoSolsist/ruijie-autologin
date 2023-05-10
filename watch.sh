#!/bin/bash
count=0
while [ $count -lt 3 ]; do 
  ping -c 1 www.baidu.com
  if [ $? -eq 0 ]; then
    count=0
    sleep 5 
 else
    python /home/mephisto/ruijie/main.py
    count=`expr $count + 1`
    sleep 10
 fi
done