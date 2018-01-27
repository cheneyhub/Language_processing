#_*_conding:uft-8_*_
'''
Version: 0.0.1
Date: 2018-01-27
@Author:Cheney
'''

'''
This program calculates the English words from 100 sentences.
In internet, it reports 100 sentences include 7000 English words, here just to verify the news.

Words data stores in "blog_en_sent_100.txt"
Program include three part: 
I-read data, II-use regular method to get words; III-calcuate the words
'''

import re

#Read data from text document
word_data = open("en_sent_100.txt")

word_list = []
sent_length = []
for line in word_data.readlines():
    #Get all the English sentences row by row
    sentence = re.findall(r"[A-Za-z]+",line)
    if sentence:
        word_list.append(sentence)
        sent_length.append(len(sentence))

print("Maxinum and minium words length of sentences:",
      max(sent_length), 'and', min(sent_length))

#Use "for" formula to get single word list from word_list
words = [word.lower() for sent in word_list for word in sent]
print ("Total words quantity: ",len(words),'\n',
       "Actual Words quantity: ",len(set(words)))
# print ("Acutal words:\n",sorted(set(words)))

#If the word length <=3, it was considered common words
common_words = [word for word in set(words) if len(word) <=3]
print ('Common words: ',len(common_words))
# print ("Common words:\n",sorted(common_words))

uncommon_words = [word for word in set(words) if word not in common_words]
print("%s English words after delete common words:\n%s" %(len(uncommon_words), sorted(uncommon_words)))

#********************End of the program***********************















