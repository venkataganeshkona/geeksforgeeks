#This code finds the maximum sum that an array can have after multiple rotations
def rotation(ar):
    temp1=ar[0]
    n=len(ar)
    #Checking edge cases
    if(n==1):
        return ar
    for i in range(0,n-1):

        ar[i]=ar[i+1]
    ar[n-1]=temp1

    return ar

def maxsum(array):

    sum=0
    n1=len(array)

    for j in range(0,n1):
        tempsum=0
        a = rotation(array)
        print a
        for k in range(0,n1):
            tempsum=tempsum+k*a[k]
            print tempsum
        if tempsum>sum:
            sum=tempsum
    print "The maximum sum is:",sum

maxsum([1,3,2])









