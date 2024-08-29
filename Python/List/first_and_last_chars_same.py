def first_and_last_chars_same(items):
    new_list=[]
    for i in items:
        if len(i)>=2:
            if i[0]==i[-1]:
                new_list.append(i)
    return len(new_list)
print(first_and_last_chars_same(["aba","xyz","1221","pqp"]))