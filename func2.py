#Second example of function
def div(x,y):
      if(x>=y):
          if(x%y==0):
              print "x is divisible by y "
          else:
              print "x is not divisible by y "
      else:
          print "The divisor is bigger than the dividend"

div(6,3)
div(6,4)
div(6,5)
print "***********************"
#Reverse a list
def rev(a):
    c=[]
    i=len(a)-1
    while i>0:
        c.append(a[i])
        i=i-1
    print c

rev([2,3,4,5,6,7,8,9])
print "***********************"
#function returning something

def is_even_odd(x):
    if(x%2==0):
        return True
    else:
        return False

print is_even_odd(4)
print is_even_odd(5)
print "***********************"

def rev(a):
    c=[]
    i=len(a)-1
    while i>0:
        c.append(a[i])
        i=i-1
    return c

z=rev([2,3,4,5,6,7,8,9])
print z

