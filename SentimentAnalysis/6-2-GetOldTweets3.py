#https://github.com/Mottl/GetOldTweets3
import string
from collections import Counter
import GetOldTweets3 as got
import matplotlib.pyplot as plt

def getTweets3(query, max_tweets, since, until):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(since).setUntil(until).setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) # it return objects
    tweets_text = [[tweet.text] for tweet in tweets]
    return tweets_text

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
query = 'corona virus'
max_tweets = 1000
since = '2018-03-15'
until = '2018-05-19'

tweets_text = getTweets3(query, max_tweets, since, until) # list
text = ''
length = tweets_text

length = len(tweets_text)
for i in range(0, length):
    text = text + tweets_text[i][0] + ''

print(text)
lowercase_text = text.lower()
clean_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))
tokenized_word = clean_text.split()
final_tokenized_word = []

for word in tokenized_word:
    if(word not in stop_words):
        final_tokenized_word.append(word)

emotions_list = []
with open('emotions.txt','r') as emotions_list_file:
    for line in emotions_list_file:
        clear_line = line.replace('\n','').replace('\'','').replace(',','').strip()
        word, emotion = clear_line.split(':')
        if word in final_tokenized_word:
                emotions_list.append(emotion)
emotion_counter = Counter(emotions_list)

fig, ax1 = plt.subplots()
ax1.bar(emotion_counter.keys(), emotion_counter.values())
fig.autofmt_xdate()
plt.savefig('twitter_emotions_' + query +'.png')
plt.show()