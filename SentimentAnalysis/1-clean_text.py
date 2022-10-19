# CTM: In NLP words are case sensitive ie "Apple" is not same as "apple"
# For NPL we need clean text which is free from uppercase letter, punctuations.
import string

text = open('sample_text1.txt', encoding='utf-8').read()
lowercase_text = text.lower()
# print(string.punctuation) # this will print all the punctuation in python string ie '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

clean_text = lowercase_text.translate(str.maketrans('', '', string.punctuation)) # args:which characters is to be replaced, With which characters that is to be replaced, characters to be deleted
print('Clean Text :\n\'', clean_text, '\'')