#This code explains the concept of for loops in python

a=[1,2,3,4,5,6,7,8,9,10]
for m in a:
    print m

#second example of for
marks=[1,2,3,4,5,6,7,8,9]
sum=0
for n in marks:
    sum=sum+n
print "The sum is =", sum
#third example of for
table_12=[12,24,36,48,60,72,84,96,108,120]
table_13=[]
z=1
for i in table_12:
    table_13.append(i+z)
    z=z+1
print "The table of 13 is \n ",table_13
