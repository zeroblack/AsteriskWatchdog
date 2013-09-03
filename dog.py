#!/usr/bin/env python

import os
import subprocess
import tweepy
import datetime
import time

popen = subprocess.Popen(['/usr/sbin/asterisk', '-rx', 'sip show peers'], stdout=subprocess.PIPE)

out, err = popen.communicate()

# fill these variables with your twitter auth data
consumer_key="your consumer key"
consumer_secret="your consumer secret"
access_token="your access token"
access_token_secret="your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for client in out.split('\n'):
   if not client.startswith('Name') and client.find('sip') == -1 and client.find('/') != -1 and client.find('OK') == -1:
      print client[:8] + client[-15:]
      #I advice you to mention your twitter handle here
      api.update_status('@yourHandle ' + client[:8] + client[-15:] + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))