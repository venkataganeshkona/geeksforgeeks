#Binary search O(logn)
def binarysearch(ar,a):
    first=0
    last=len(ar)-1
    flag=0
    mid=0

    while first<last and flag==0:
        mid = (first + last) / 2
        if(ar[mid]==a):
            flag=1
        else:
            if a<ar[mid]:
                last=mid-1
            else:
                first=mid+1
    if(flag==0):
        print "Element not found"
    else:
        print "Element found at ",mid," index"

binarysearch([1,2,3,4,5,6,7,8],7)


