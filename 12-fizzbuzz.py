#For multiples of three print Fizz instead of the number and for multiples of five print Buzz.

def fixxbuzz():
	for i in range (1, 101):
		print(i, end=" ")
#end places the items in horizontal format

fixxbuzz()
print()
print()


def fixxbuzz():
	for i in range (1, 101):
		if i % 15 == 0:
			print ("FizzBuzz", end=" ")
		elif i % 3 == 0:
			print ("Fizz", end=" ")
		elif 1 % 5 == 0:
			print ("Buzz", end= " ")
		else:
			print (i, end=" ")
fixxbuzz()

