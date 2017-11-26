#This code explains the concept of class in python

class square():
    pass
x=square()
x.side=14
print x.side

#another example of class

class square():
    def perimeter(self,side):
        return side*4
a=square()
print a.perimeter(14)

#another example
class student():
    def __init__(self,name):
            self.name=name
a=student("Sam")
print a.name

#another example
class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

a=rectangle(2,4)
print a.area()
print a.perimeter()