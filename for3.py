#Another example of for loop(To find prime numbers)
for i in range(10,20):
    for j in range(2,i):
        if (i%j==0):
            k=i/j
            print "%d is equal to %d * %d " %(i,j,k)
            break
    else:
        print i," is a prime number"


