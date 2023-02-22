#when you use global keyword it forces python to refrain from creating a new variable 
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)