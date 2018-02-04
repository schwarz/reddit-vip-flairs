"""
Automatically flair submissions with comments by interesting people.
"""

from dotenv import load_dotenv, find_dotenv
import logging
import praw
import os

def main():
    load_dotenv(find_dotenv())
    client_id = os.getenv('VIP_CLIENT_ID')
    client_secret = os.getenv('VIP_CLIENT_SECRET')
    flair_text = os.getenv('VIP_FLAIR_TEXT')
    flair_text_sep = os.getenv('VIP_FLAIR_TEXT_SEP', ' | ')
    username = os.getenv('VIP_USERNAME')
    password = os.getenv('VIP_PASSWORD')
    vips = os.getenv('VIP_VIPS').split(',')
    subreddit = os.getenv('VIP_SUBREDDIT')
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                    password=password, user_agent="reddit-vip-flairs",
                    username=username)

    for comment in reddit.subreddit(subreddit).stream.comments():
        submission = comment.submission
        if (submission.author in vips and
           (not submission.link_flair_text or flair_text not in submission.link_flair_text)):
            try:
                new_text = flair_text
                # Append if flair text already set
                if submission.link_flair_text:
                    new_text = "{}{}{}".format(
                            submission.link_flair_text,
                            flair_text_sep, flair_text)

                data = {'link': submission.fullname, 'text': new_text,
                        'css_class': submission.link_flair_css_class}
                reddit.post("/r/{}/api/flair".format(subreddit), data)
                logging.info('assigned flair to submission {} triggered by comment {}'.format(comment.link_id, comment.id))
            except:
                logging.error('flair update triggered by comment {} failed'.format(comment.id))

if __name__ == "__main__":
    main()

