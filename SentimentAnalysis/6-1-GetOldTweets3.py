#https://github.com/Mottl/GetOldTweets3
import GetOldTweets3 as got

#Get tweets by username(s):
def getTweets1(usernames, max_tweets):
    tweetCriteria = got.manager.TweetCriteria().setUsername(usernames).setMaxTweets(max_tweets) # used setUsername()
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    return tweet.text # we are actuall return only first tweet

#Get tweets by query search:
def getTweets2(query, max_tweets, since, until):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(since).setUntil(until).setMaxTweets(1) # used setQuerySearch()
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    return tweet.text

#Get tweets by username and bound dates and preserve emojis as unicode:
def getTweets3(usernames, max_tweets, since, until):
    tweetCriteria = got.manager.TweetCriteria().setUsername(usernames).setSince(since).setUntil(until).setMaxTweets(1).setEmoji("unicode") # used setUsername()
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    return tweet.text

#Get the last 10 top tweets by username:
def getTweets4(usernames, max_tweets):
    tweetCriteria = got.manager.TweetCriteria().setUsername(usernames).setTopTweets(True).setMaxTweets(max_tweets) # used setUsername()
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    return tweet.text

print()
max_tweets = 2
usernames = 'barackobama whitehouse'
print('getTweets1(usernames, max_tweets):\n', getTweets1(usernames, max_tweets), end='\n\n\n') # for multiple users user blank space

usernames = 'barackobama'
since = '2015-05-01'
until = '2015-06-25'

print('getTweets1(usernames, max_tweets):\n', getTweets1(usernames, max_tweets), end='\n\n\n')
query = "european refugee"
print('getTweets2(usernames, max_tweets, since, until):\n', getTweets2(usernames, max_tweets, since, until), end='\n\n\n')
print('getTweets3(usernames, max_tweets, since, until):\n', getTweets3(usernames, max_tweets, since, until), end='\n\n\n')
print('getTweets4(usernames, max_tweets):\n', getTweets4(usernames, max_tweets), end='\n\n\n')
