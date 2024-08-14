def remove_odd_indexed(str1):
    even_indexed=" "
    for i in str1:
        if str1.index(i)%2==0:
            even_indexed+=i
    return even_indexed
print(remove_odd_indexed("python"))