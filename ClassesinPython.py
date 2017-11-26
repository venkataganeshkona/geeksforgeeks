#These codes will explain the concept of classes python

class MyClass:
    variable="blah"

    def function(self):
        print "This is a message inside the class !"

m1=MyClass()
m2=MyClass()

m2.variable="blahblah"
print m1.variable
print m2.variable

print m1.function()
print m2.function()