l=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(i for i in l))

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

x=8
print(fact(x))

n=int(input("Enter the number"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)

num=input("Enter the sequence of numbers.")
l=num.split(',')
print(num)
print(l)
print(tuple(l))
              
