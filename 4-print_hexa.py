#Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

for i in range (0, 98):
    print(f"{i} = 0x{i}")
# here we use hexadecimal
for i in range(0, 99):
    print(f"{i} = {hex(i)}")

# must be separated by ,, followed by a space: should be printed in ascending order, with two digits: 
for i in range (0, 10):
    print(f"0{i},")
for i in range(10, 99):
    print(f"{i},")


#another way

#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print("{:0>2d}".format(i), end=", ")
