secret_number = 5
number = int(input("Enter a number = "))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter the number again: "))
secret_number = 5
print(secret_number)
print("Well done, muggle! You are free now.")