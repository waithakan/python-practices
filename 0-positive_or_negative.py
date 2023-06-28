#The output of the program should be:
#The number, followed by
#if the number is greater than 0: is positive
#if the number is 0: is zero
#if the number is less than 0: is negative
#followed by a new line


#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(f"{number} Is positive")
elif number == 0:
    print (f"{number} is zero")
else:
   print(f"{number} is negative")
