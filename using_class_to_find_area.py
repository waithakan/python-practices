length = int(input("Please enter lenght of rectangle: "))
width = int(input("Please enter width of rectangle: "))

class Rectangle: #we must declare class first
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return(self.length * self.width)
    def perimeter(self):
        return(2*(self.length + self.width))

r = Rectangle(length, width)  #declaring a methob(instance of a class)
print ("Area is: ", r.area())
print("Perimeter is: ", r.perimeter())
