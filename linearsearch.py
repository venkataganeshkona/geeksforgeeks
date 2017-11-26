#Linear search:O(n) time complexity

def linearsearch(ar,a):
    flag=0
    index=0
    for i in range(0,len(ar)):
        if a==ar[i]:
            flag=1
            index=i
    if flag==1:
        print "Element found at ",index," index"
    else:
        print "Elemnet not found"

linearsearch([1,2,3,4,5,6],5)

