#This code explains teh concepts of subclass in python

class rect():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

class square(rect):
    def __init__(self,side):
        rect.__init__(self,side,side)
        self.side=side

s=square(4)
print s.length
print s.breadth
print s.side
print s.area()
