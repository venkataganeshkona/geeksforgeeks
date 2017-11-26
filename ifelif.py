#This code explains if and elif
print "Enter a number:"
x=input()
if (x%2==0):
    if (x>10):
        print "The number is even and greater than 10"
    else:
        print "The number is even but not greater than 10"
elif (x%2!=0):
    print "The number is odd"