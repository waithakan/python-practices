while True:
	try:
		x = int(input("Please enter a number: "))
		break 
	except ValueError:
		print("Oops! That was no valid number. Try again . . ")

# First, the try clause (the statement(s) between the try and except keywords) is executed.
# if no error  the exception is skipped  and  executes.
#
 
