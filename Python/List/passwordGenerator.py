import random
n=int(input("Enter the length of the password"))

choices_i_have=list("abcdefghijklmnopqrstuvwxyz")

caps=input("Do you want capital lettes (y/n)?")
if caps=="Y" or caps=="y":
    choices_i_have.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

nums=input("Do you want numbers in your password (y/n)?")
if nums=="Y" or nums=="y":
    choices_i_have.extend(list("0123456789"))

symbols=input("Do you want symbols in your password (y/n)?")
if symbols=="Y" or symbols=="y":
    choices_i_have.extend('''!@#$%^&*()<>??{}|''')

password=""

for i in range(n):
    choosen=random.choice(choices_i_have)
    password+=choosen

print(password)