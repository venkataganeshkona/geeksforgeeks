#this code explains the concepts of recursion
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)

print fact(5)
print fact(0)
print fact(1)