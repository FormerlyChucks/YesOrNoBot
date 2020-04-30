import praw
from random import choice
import re
import time

reddit = praw.Reddit(user_agent='USER AGENT',
                  client_id='CLIENT ID',
                  client_secret='SECRET',
                  username='USERNAME',
                  password='PASSWORD')

with open("YesOrNo.txt") as f:
    lines = [l.rstrip() for l in f]

subreddit = reddit.subreddit('SUBREDDIT')

for submission in subreddit.stream.submissions():
    if re.search("!YesOrNo", submission.title, re.IGNORECASE):
        submission.reply(choice(lines))
