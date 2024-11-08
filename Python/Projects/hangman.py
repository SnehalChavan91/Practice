import random
from collections import Counter

fruits='''apple,banana,cherry,berry,watermelon,muskmelon,lemon,jamun,pineapple,guava,orange'''
fruits=fruits.split(",")

fruit=random.choice(fruits)
print(fruit)

chances=len(fruit)+2
guessedFruit=" "
if chances:
    while chances>0:
        chances-=1
        guess=input("Enter the character of the guessed fruit ")
        if guess in fruit:
            k=fruit.count(guess)
            for _ in range(k):
                guessedFruit+=guess

        for char in fruit:
            if (Counter(fruit)==Counter(guessedFruit)):
                print("The fruit is ",fruit)
                print("You win !")
                break
                break
            elif char in guessedFruit and (Counter(fruit)!=Counter(guessedFruit)):
                print(char,end=" ") 
                continue
            else:
                print("_",end=" ")
        
elif not chances and (Counter(fruit)!=Counter(guessedFruit)):
    print("You lost! Try again.")
    print("The fruit is {}".format(fruit))

    