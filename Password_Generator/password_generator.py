import random
import string

print("===== Password Generator =====")

while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)