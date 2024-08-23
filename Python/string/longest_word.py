def longest_word(words):
    words_list=[]
    for i in words:
        words_list.append((len(i),i))
        words_list.sort()
    print(words_list)
    return words_list[-1][0]

words=["good","better","best"]
print(longest_word(words))