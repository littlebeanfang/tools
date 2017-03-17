#!/bin/bash
echo "Fetch free accounts from ishadowsocks..."
python crawler.py
echo "Kill running sslocal..."
ps aux | grep 'sslocal' | grep -v 'grep' | cut -c 9-15 | xargs kill -9
echo "Restart sslocal..."
sslocal -c iss.json
