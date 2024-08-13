def remove_char(str,n):
    str1=str[:n]
    str2=str[n+1:]
    return str1+str2
print(remove_char("python",0))
print(remove_char("python",2))
print(remove_char("python",3))
print(remove_char("python",4))
print(remove_char("python",5))
