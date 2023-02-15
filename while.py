'''
secret_number = 5
number = int(input("Enter a number = "))
while number != secret_number:#while number is not secret number
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter the number again: "))
secret_number = 5
print(secret_number)
print("Well done, muggle! You are free now.")
'''
while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")