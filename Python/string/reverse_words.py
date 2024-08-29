def reverse_words(sentence):
    for i in sentence:
        splited_sentence=sentence.split(" ")
        reverse_sentence=splited_sentence[::-1]
        new_sentence=" ".join(reverse_sentence)
        
    print(new_sentence)
    
print(reverse_words("Python is a programming language"))