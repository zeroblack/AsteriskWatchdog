#!/usr/bin/env python

import os
import subprocess
import tweepy
import datetime
import time
import argparse

# Check config options
parser = argparse.ArgumentParser(description='Tweet an alert when a PBX extension goes down')
parser.add_argument('--notweet', help='Active when a tweet alert should be triggered', action='store_true')
parser.add_argument('--ck', help='Consumer key')
parser.add_argument('--cs', help='Consumer secret')
parser.add_argument('--at', help='Access token')
parser.add_argument('--ats', help='Access token secret')

args = parser.parse_args()

print args
# Check PBX extensions status
popen = subprocess.Popen(['/usr/sbin/asterisk', '-rx', 'sip show peers'], stdout=subprocess.PIPE) 
out, err = popen.communicate()

# Twitter config data
consumer_key=args.ck
consumer_secret=args.cs
access_token=args.at
access_token_secret=args.ats
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Trigger needed alerts
for client in out.split('\n'):
   if not client.startswith('Name') and client.find('sip') == -1 and client.find('/') != -1 and client.find('OK') == -1:
      print client[:8] + client[-15:]
      if not args.notweet:
         api.update_status('@sdrgalvis ' + client[:8] + client[-15:] + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
