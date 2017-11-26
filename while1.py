#This code explains the usage of while and if and else

more=True
while more==True:
    print "Enter your details:"
    name=raw_input("Enter your name>>>")
    eng=input("Enter your marks in english>>>")
    math=input("Enter your marks in maths>>>")
    sci=input("Enter your marks in science>>>")
    comp=input("Enter your marks in computer>>>")
    total=eng+math+sci+comp
    percentage=(total/400.0)*100
    print name," Your total marks is= ",total," and your percentage= ",percentage

    a=raw_input("Do want to enter again? Press Y/N>>>")
    if(a=='Y'):
        more=True
    else:
        more=False

