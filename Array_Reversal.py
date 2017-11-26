#Array reversa in Place O(n)

def array_reversal(a):

    N=len(a)

    if(N%2==0):
       mid=N/2

       for i in range(0,mid):
           temp=a[i]
           a[i]=a[N-1-i]
           a[N-1-i]=temp

    elif(N%2==1):
        mid=(N+1)/2

        for i in range(0, mid):
            temp = a[i]
            a[i] = a[N - 1 - i]
            a[N - 1 - i] = temp

    return a

a=[1,2,3,4,5,6,7,8,9]

reversed_array=array_reversal(a)

print reversed_array