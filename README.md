# naidunia-epaper-downloder

This solution is dedicated to my dad. This script works well on **linux.**

## Dependencies
-	**PyPDF2** : **`pip install PyPDF2`**.
-	**python-telegram-bot**: **`pip install python-telegram-bot`**

Join channel on Telegram: [**@NaiDunia**](http://t.me/NaiDunia)

## What this script does?
-	It downloads all pages of newspaper, which are separate. 
-	Then it merge them.
-	And finally uploads to telegram.

## Deployed on:
-	~~**Heroku**: using [this method](https://github.com/michaelkrukov/heroku-python-script)~~
-	**AWS EC2** instance as crontab-job: `0 6 * * * ~/miniconda3/bin/python ~/naidunia-bot.py`