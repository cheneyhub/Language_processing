#_*_conding:uft-8_*_
'''
Version: 0.0.1
Date: 2017-12-26
@Author:Cheney
'''

'''
Statistic the most used English words in one news from Xinhua net.
Mode I:News has been download to local saved as "new_xinhua.txt"
News source: http://www.xinhuanet.com/english/2017-12/27/c_136853671.htm

Analysis:
1. Open file use 'Open()' or "With open() as "
2. Calculate the words frequency, it can use dict, key is word and value is the frequency figure.
3. Before calculate words, it need to use regular method to get the single words.
4. Words in the dict need to sort, it use "sort()" or "sorted()", sorted() is faster.

'''

# Program start.
import re
import io

#Define a class to process text and calculate words frequency
class CounterWords():
    #Read text file and save the words in dict
    def __init__(self,path):
        self.word_dict = dict()

        #If use file name but not path it can use "with open()" but not "with io.open()"
        with io.open(path,encoding="utf-8") as f:
            data = f.read()
            words = [single.lower() for single in re.findall("\w+", data)]
            for word in words:
                self.word_dict[word] = self.word_dict.get(word,0) + 1 #Very good pythonic

    #Calculate the top used words frequency
    def word_frequency(self,n):
        assert n > 0, "n should be large than 0"
        word_sort = sorted(self.word_dict.items(), key=lambda item:item[1], reverse=True)
        return word_sort[:n]


if __name__ == "__main__":
    print('Life is short, use Python in life ')

    top_commom_word = CounterWords('news_xinhua.txt').word_frequency(10)
    print ("The top used words:")
    for word in top_commom_word:
        print (word)






