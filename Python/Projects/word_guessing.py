import random
words='''apple banana cherry watermelon berry muskmelon orange'''
words=words.split(" ")
print(words)
word=random.choice(words)
chances=len(word)+2
guessed=" "
while chances>0:
    failed=0
    guess=input("Enter the guessed character ")
    guessed+=guess

   # fruit=input("Enter the guessed character from fruit name ")
    for char in word:
        if char in guessed:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win")
        print("The word is : ",word)
        break


    if guess not in word:
        chances-=1
        print("Wrong guess")
        print("You have ",+chances," more guesses")

        if chances==0:
            print("You loose")
    
    
