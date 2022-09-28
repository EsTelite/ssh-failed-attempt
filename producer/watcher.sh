#!/bin/sh
cp ../send-event-util/watcher.py ~/watcher.py
if pgrep -a python | grep 'watcher.py'
then
    echo "Watcher already running"
else
  python3 ~/watcher.py &
fi