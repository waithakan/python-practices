#import def add(a, b) from  add_0.py 
def add(a, b):
	a = 1
	b = 2
	return a + b

print(add(1, 2))


#correctio
if __name__ == "__main__":
	from add_0 import add
	a = 1
	b = 2
	print(f"{a} + {b} = ", add(a, b))
