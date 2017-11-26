#Method 2 Using a temp variable and left shifting one by one
def arrayrot2(ar,d,n):
    for i in range(0,d):
        temp=ar[i]
        for j in range (i+1,n):
            temp1=ar[j]
            ar[j-1]=temp1
        #print ar
        ar[n-1]=temp
        #print ar
    print ar
arrayrot2([1,2,3,4,5],2,5)
