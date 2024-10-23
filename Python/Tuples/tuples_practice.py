thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)


p=("kiwi",)
thistuple+=p
print(thistuple)
l=list(thistuple)
l.remove("banana")
print(tuple(l))

for i in l:
    print(i)

for i in range(len(l)):
    print(l[i])
