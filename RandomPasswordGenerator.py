import random
import string

def generate(length):
    characters= string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password
while True:
    length=int(input("Enter the length of the passwords:"))
    password=generate(length)
    print("Your random password is:",password)
    next=input("let's do next calculation?(yes/no):")
    if next == "no":
        break
    else:
        print("Invalid input")