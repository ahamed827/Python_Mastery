import random
import string

def make_password():
    length=int(input("Enter Password length: "))
    if length<4:
        print("Password length must be atleast 4")
        return
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    symbols=string.punctuation
    password=[random.choice(upper),
              random.choice(lower),
              random.choice(digits),
              random.choice(symbols)]
    all_chars=upper+lower+digits+symbols
    for i in range(length-4):
        random_char=random.choice(all_chars)
        password.append(random_char)
        random.shuffle(password)
    final_password="".join(password)
    print("Generate Password: ",final_password)
print("--Random Password Generator--")
while True:
    make_password()
    print()
    choice=input("Do you want another password?(y/n):").lower()
    if choice!="y":
        print("Goodbye! Stay safe online.")
        break
    print()

