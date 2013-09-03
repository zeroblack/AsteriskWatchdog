# AsteriskWatchdog

Tweet an alert whenever a PBX extension goes down

You will run this script using crontab. every time it runs, it will tweet you whether a PBX extension went down.

## Usage
Fill the OAuth fields inside _dog.py_

You will need to install [Tweepy](https://github.com/tweepy/tweepy "Tweepy") first.

Then add edit crontab and make _dog.py_ run every minute for example.

 