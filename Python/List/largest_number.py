def largest_num(items):
    for i in items:
        max=items[0]
        for i in items:
            if i>max: #ignore:type
                max=i
    return max 
print(largest_num([10,40,24,50,48]))