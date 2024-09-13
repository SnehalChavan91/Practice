lst=[1,2,1,3,1,4,3,5,4,6]
duplicate_items=set()
unique_items=[]
for i in lst:
    if i not in duplicate_items:
        unique_items.append(i)
        duplicate_items.add(i)
print(unique_items)