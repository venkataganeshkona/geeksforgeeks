#This code explains Kadane's algo
print "Enter the number of test cases:"
t=input() #number of test cases
for i in range (1,t+1):
    print "Enter the size of the array:"
    n=input() #size of array
    ar=map(int,(raw_input().strip().split(' ')))

    globalmax=0
    #Code logic begins
    if(n==1):
        globalmax=ar[0]
    else:
        for j in range(0,n):
            globalmax=ar[i]
            sum=ar[i]
            max=sum
        for k in range(j+1,n):
            sum=sum+ar[k]
            if sum>max:
               max=sum
        if max>globalmax:
            globalmax=max
    print globalmax





