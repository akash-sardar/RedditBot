import praw
import prawcore


reddit = praw.Reddit(
    client_id = '',
    client_secret = '',
    password = '',
    user_agent = '',
    username = '',
    ratelimit_seconds=600
)

def limitRates():
    pass

def ReadReddit(subname):
    while True:
        try:
            subreddit = reddit.subreddit(subname)
            for submission in subreddit.top(time_filter = 'day'):
                if submission.score > 10:
                    print(submission.title,submission.selftext,submission.url, submission.score, sep='\n')
                    print('\n\n')

            break
        except AttributeError as e:
            print('Attribute Error: ', e)
        except prawcore.PrawcoreException as e:
            print('Please enter a valid subreddit', e)
        except NameError as e:
            print('NameError', e)



def main():
    # Create a submission to r/test
    #reddit.subreddit('test').submit('test submission', url = 'https://reddit.com')
    # Comment on a known submission
    # submission = reddit.submission(url="https://www.reddit.com/r/test/comments/186wzw9/test_submission/")
    # submission.reply("Super rad!")
    subname = 'Python'
    ReadReddit(subname)



if __name__=='__main__':
    main()



