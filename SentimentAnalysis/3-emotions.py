# CTM: In NLP words are case sensitive ie "Apple" is not same as "apple"
# For NPL we need clean text which is free from uppercase letter, punctuations.
import string

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

text = open('sample_text1.txt', encoding='utf-8').read()
lowercase_text = text.lower()
clean_text = lowercase_text.translate(str.maketrans('', '', string.punctuation)) # args:which characters is to be replaced, With which characters that is to be replaced, characters to be deleted

tokenized_word = clean_text.split()
final_tokenized_word = []

for word in tokenized_word:
    if(word not in stop_words):
        final_tokenized_word.append(word)

with open('emotions.txt','r') as emotions_list: # reading line by line
    for line in emotions_list:
        clear_line = line.replace('\n','').replace('\'','').replace(',','').strip() # this will result in fromat => word : emotion
        word, emotion = clear_line.split(':')
        print("word :", word, "emotions :", emotion)