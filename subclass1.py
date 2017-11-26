#This code explains the concept of subclass of a class
class child():
    def __init__(self,name):
        self.name=name
class student(child):
    def __init__(self,name,roll):
        self.roll=roll
        child.__init__(self,name)

a=child("xyz")
print a.name
b=student("abc",12)
print b.name
print b.roll