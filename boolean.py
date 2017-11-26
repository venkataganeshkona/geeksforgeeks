#This code explains the concepts of boolean
print "Enter first number :"
x=input()
print "Enter second number :"
y=input()
print x==y

#---------------------------------------------
print "Enter first number :"
x=input()
print "Enter second number :"
y=input()
print "Enter third number :"
z=input()
all1=(x == y) and (x == z) and (y == z)
print "All are equal",all1
all2=(x == y) or (x == z) or (y == z)
print "Any of two are equal",all2
#----------------------------------------------
passmarks=35
print "Enter your marks:"
marks=input()
print marks>passmarks