import random
num=random.randrange(1000,10000)
print(num)

n=int(input("Enter the 4 digit number"))

if(n==num):
    print("Congratulations! You are a mastermind")

else:

    correct=[]

    n=str(n)
    num=str(num)
    ctr=0

    while n!=num:
        ctr+=1
        count=0
        for i in range(0,4):
            if n[i]==num[i]:
                count+=1
                correct.append(n[i])
            else:
                continue
        if (count<4) and (count!=0):
            print("You get ",count," numbers correctly.")
            for k in correct:
                print(k,end=" ")
            
            n=int(input("Enter your next number"))
            n=str(n)
        elif count==0:
            print("None of the numbers from your guess are correct")
            n=int(input("Enter your next choice of digit"))
            n=str(n)
    if n==num:
        print("You are a mastermind!")
        print("You guessed number in ",ctr+1,"tries")
