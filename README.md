# AsteriskWatchdog

Tweet an alert whenever a PBX extension goes down

You will run this script using crontab. every time it runs, it will tweet you whether a PBX extension went down.

## Usage
- You will need to install [Tweepy](https://github.com/tweepy/tweepy "Tweepy") first.

- Pass your twitter OAuth credentials as parameters:
  
./dog.py --ck=YourConsumerKey --cs=YourConsumerSecre --at=YourAccessToken --ats=YourAccessTokenSecret

Bonus: You can use crontab and make _dog.py_ run every minute for example.

