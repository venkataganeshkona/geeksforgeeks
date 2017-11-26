#Strings 2
import string
print "Enter your string"
a=raw_input()
if a>"abc":
    print "Your word comes after abc"
elif a<"abc":
    print "Your world comes after abc"
else:
    print "Your world is abc"

#-----------------------------------------
#String functions
print "Enter your numbers"
b=raw_input()
c=b.split()
print c
d=map(int,c)
print d

