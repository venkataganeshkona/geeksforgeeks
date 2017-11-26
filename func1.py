#This code explains the concept of functions in python
def is_even(x):
    if (x%2==0):
        print "The number is even"
    else:
        print "The number is not even"
is_even(112)
is_even(117)
#-------------------------------------
def print_poem():
    print "I am the lord of the rings!!"
    print "I will rule this world one day!!"

print_poem()

#------------------------------------
def print_sum():
    a=input("Enter your first number>>")
    b=input("Enter your second number>>")
    print a+b

print_sum()
