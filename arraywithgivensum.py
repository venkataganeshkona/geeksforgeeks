#RotatedArray with given sum

def arraywithsum(ar,sum):
    n=len(ar)
    flag=0
    temp=0
    sumtobf=sum
    for i in range(0,n-1):
        temp=ar[i]
        add=0
        for j in range(i+1,n):
            add=temp+ar[j]
            if add==sumtobf:
                flag=1
                break
            add=ar[i]
    if (flag==1):
        print "Pair found"
    else:
        print "Pair not found"

arraywithsum([11, 15, 26, 38, 9, 10],45)




