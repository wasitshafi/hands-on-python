from nltk.corpus import twitter_samples

"""
positive_tweets = twitter_samples.strings('positive_tweets.json') # strings() method will print all of the tweets within a dataset as strings
negative_tweets = twitter_samples.strings('negative_tweets.json')
#text = twitter_samples.strings('tweets.20150430-223406') # 20000 Tweets with no sentiments

print('Positive Tweets : ', positive_tweets) # 5000 Positive Tweets
print('Total Positive Tweets : ', len(positive_tweets))
for i in range(1, 10):
    print()

print('Negative Tweets : ', positive_tweets) # 5000 Negative Tweets
print('Total Negative Tweets : ', len(positive_tweets))
for i in range(1, 10):
    print()

#print('Tweets with No sentiment : ', text) # 5000 Negative Tweets
"""

positive_tweets_tokenized = twitter_samples.tokenized('positive_tweets.json')
#negative_tweets_tokenized = twitter_samples.tokenized('negative_tweets.json')

"""
print("Positive tokenized tweets are as : ")
for ttweets in positive_tweets_tokenized:
    print(ttweets)
"""
print("Positive tokenized tweets are as : ")
for ttweets in positive_tweets_tokenized:
    for word in ttweets:
        print(word)
