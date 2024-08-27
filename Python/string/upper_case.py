# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def uppercase(str1):
    num_upper=0
    for i in str1[:4]:
        if i.isupper():
            num_upper+=1
    print(num_upper)
    if num_upper>=2:
        return str1.upper()
    return str1
print(uppercase("PYTHon"))
print(uppercase("PyTHon"))
str1="PYTHon"
print(uppercase(str1))