import random
import string

def generate_password(length,include_digits=True,include_special=True):
    letters=string.ascii_letters
    digits=string.digits
    special_chars=string.punctuation

    char_pool=letters

    if include_digits:
        char_pool+=digits
    if include_special:
        char_pool+=special_chars

    password=''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    try:
        length=int(input("Enter the length of the password"))
    except ValueError:
        print("Invalid input. Please enter the number.")
        return

    include_digits=input("Include digits?(y/n): ").lower()=='y'
    include_special=input("Include special characters?(y/n): ").lower()=='y'

    password=generate_password(length,include_digits,include_special)

    print(f"Generated password: {password}")

if __name__=="__main__":
     main()