#This code takes input from user
print "This code will take 10 numbers as i/p"
a=[]
i=0
while(i<10):
    print "Enter next number:"
    num=input()
    a.append(num)
    i=i+1
sum=0
j=0
while(j<10):
    sum=sum+a[j]
    j=j+1
print sum

