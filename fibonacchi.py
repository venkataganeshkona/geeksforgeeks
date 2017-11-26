#This code explains the concept of fibonacchi
prev={0:0,1:1}
def fibo(n):
    if prev.has_key(n):
        return prev[n]
    else:
        f1=fibo(n-1)+fibo(n-2)
        prev[n]=f1
        return f1

print fibo(0)
print fibo(1)
print fibo(2)
print fibo(3)
print fibo(4)
