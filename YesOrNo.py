import praw, time, random, traceback

reddit = praw.Reddit(user_agent='USER AGENT',
                     client_id='CLIENT ID',
                     client_secret='SECRET',
                     username='USERNAME',
                     password='PASSWORD')

def getResponse():
    number = random.randrange(1, 1000000)
    if number == 1000000:
      return "B&"
    elif number == 999999:
      return "PLATINUM AWARD"
    elif number == 999998:
      return "GOLD AWARD"
    elif number == 999997:
      return "SILVER AWARD"
    else:
        if number % 2 == 0:
          return "Yes"
        else:
          return "No"
        
while True:
    try:
        for submission in reddit.subreddit('SUBREDDIT').stream.submissions(skip_existing=True):
            if "!YesOrNo" in submission.title.lower():
                response = getResponse()
                submission.reply(response)
                if response == "B&":
                  reddit.subreddit.banned.add(submission.author.name, ban_reason="You got 'B&' as a response.")  # Ban the post author. 
                elif response == "PLATINUM AWARD":
                  submission.gild("gid_3") # Give a platinum award to the post.
                elif response == "GOLD AWARD":
                  submission.gild("gid_2") # Give a gold award to the post.
                elif response == "SILVER AWARD":
                  submission.gild("gid_1") # Give a silver award to the post.
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
