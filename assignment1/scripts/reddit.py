import os
import praw
import csv
from datetime import datetime

reddit = praw.Reddit(
    client_id="A4kAJLjEOAIdDCZKhYmDQg",
    client_secret="dfMn_2hKqiIpHI9liSkGT541AynfLw",
    user_agent="testscript by u/fakebot3",
    check_for_async=False,
)
reddit.read_only = True

keywords = ["electric vehicle", 'EV']
subreddits = ["electricvehicles", "electriccars"]

def fetch_reddit_data():
  data = []
  for subred in subreddits:
      subreddit = reddit.subreddit(subred)
      for keyword in keywords:
          for submission in subreddit.search(keyword, limit=50):
            data.append({
                'keyword': keyword,
                'subreddit': subred,
                'title': submission.title,
                'author': submission.author,
                'body': submission.selftext,
                'date': datetime.fromtimestamp(submission.created_utc),
                'upvotes': submission.score,
            })
  return data

def save_to_csv(data, headers, path_str, filename):
  if not os.path.exists(path_str):
      os.makedirs(path_str)
  filepath = os.path.join(path_str, filename)
  with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
    print(f"Data saved to {filepath}")


reddit_data = fetch_reddit_data()
reddit_csv_headers = ['keyword', 'subreddit', 'title', 'author', 'body', 'date', 'upvotes']
save_to_csv(reddit_data, reddit_csv_headers , 'datasets/raw/', 'reddit_posts.csv')
