import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_score(sentiment_text)
    #print(score)
    pos = score['pos']
    neg = score['neg']

    if pos > neg:
        print('Positive Sentiment')
    elif neg > pos:
        print('Negative Sentiment')
    else:
        print('Neutral Vibe')

text = open('sample_text1.txt', encoding = 'UTF_8').read()
lower_text = text.lower()

cleaned_text = lower_text.translate(str.maketrans("", "", string.punctuation))
sentiment_analysis(cleaned_text)