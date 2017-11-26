#This code explains the concept of method override

class rectangle():
    def __init__(self,len,br):
        self.length=len
        self.breadth=br

    def getarea(self):
        print self.length*self.breadth," is area of the rectangle"

class square(rectangle):
    def __init__(self,side):
        self.side=side
        rectangle.__init__(self,side,side)
    def getarea(self):
        print self.side*self.side," is are of the square"

s=square(4)
r=rectangle(4,2)
s.getarea()
r.getarea()