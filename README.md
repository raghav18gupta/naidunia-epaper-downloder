# naidunia-epaper-downloder

This solution is dedicated to my dad. This script works well on **linux.**

## Dependencies
-	**PyPDF2** using **`pip install PyPDF2`**.
-	**telegram** using **`pip install python-telegram-bot`**

Join channel on Telegram: **@NaiDunia**

### What this script does?
-	And finally uploads to telegram.
-	It downloads all pages of newspaper, which are separate. 
-	Then it merge them.

### Deployed on:
-	~~Heroku: using [this](https://github.com/michaelkrukov/heroku-python-script)~~
-	AWS EC2 instance as cron-job: `0 6 * * * ~/miniconda3/bin/python ~/naidunia-bot.py`