'''
for index in range(5):
    print(index)#print numbers from 0 to 4

for index in range(1,6):
    print(index)#print numbers from 1 to 5

for index in range(0, 11, 2):
    print(index)#print numbers from 0 to 4
'''
import time
for i in range (1, 6):#range from 1 to 6
    print(i, "MIssissipi")
    time.sleep(2)#timer after every 2 second an execution occur
print("Ready or not here i come")#output after the 5 execution are met



2. 

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)
    
