#This code explains the use of rage and length funcctions


print range(1,5)
print range(10)
print range(1,11)
print range(0)
print range(1,10,2)

#------------------------------
b=range(1,5)
print len(b)
#------------------------------
c=range(1,10)
d=len(c)
sum=0
i=0
while (i<d):
    sum=sum+c[i]
    i=i+1
print sum
