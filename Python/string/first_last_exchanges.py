def exchange_chars(str1):
    char1=str1[0]
    char2=str1[-1]
    return char2+str1[1:-1]+char1
print(exchange_chars("python"))