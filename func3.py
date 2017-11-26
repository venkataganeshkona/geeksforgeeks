#example of functions
def is_even(x):
    if(x%2==0):
        return True
    else:
        return False

def is_div_6(y):
    if(is_even(y) and y%3==0):
        print "Number is divisible by 6"
    else:
        print "Number is not divisible by 6"

is_div_6(7)
#is_div_6(12)