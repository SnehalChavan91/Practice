import math
def longest_word(words):
    words_list=[]
    for i in words:
        words_list.append((len(i),i))
        words_list.sort()
    return words_list[-1][0],words_list[-1][1]
words=input("Enter the words")
words=words.split()
print(longest_word(words))


