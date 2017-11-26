#Method 1,O(n),O(d)-->using a temp array
def arrayrot1(ar,d,n):
    temp=[]

    for i in range(0,d):
        temp.append(ar[i])
    print temp

    k=d
    for j in range(d,len(ar)):
        ar[j-k]=ar[d]
        d=d+1
    print ar

    m=0
    for l in range(n-k,n):
        ar[l]=temp[m]
        m=m+1
    print ar


arrayrot1([1,2,3,4,5,6,7],2,7)
