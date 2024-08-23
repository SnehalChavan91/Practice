def longest_word(sentence):
    words=sentence.split(" ")
    print(words)
    new_word=[]
    for i in words:
        new_word.append((len(i),i))
        new_word.sort()
    print(new_word)
    print(new_word[-1][0])
longest_word("I am a python developer")
