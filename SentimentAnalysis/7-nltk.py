import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from collections import Counter

text = open('sample_text1.txt', encoding = 'UTF_8').read()
lower_text = text.lower()

cleaned_text = lower_text.translate(str.maketrans("", "", string.punctuation))
tokenized_words = word_tokenize(cleaned_text)

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotions_list = []
with open('emotions.txt','r') as emotions_list_file:
    for line in emotions_list_file:
        clear_line = line.replace('\n','').replace('\'','').replace(',','').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
                emotions_list.append(emotion)
emotion_counter = Counter(emotions_list)

fig, ax1 = plt.subplots()
ax1.bar(emotion_counter.keys(), emotion_counter.values())
fig.autofmt_xdate()
plt.savefig('emotions-7-nltk.png')
plt.show()