#This code explains the use of while/break

while True:
    print "Enter your details>>"
    name=raw_input("Enter your name>>")
    math=input("Enter your marks in Maths>>")
    sci=input("Enter your marks in Science")
    eng=input("Enter your marks in English")
    comp=input("Enter your marks in Computer")
    total=math+sci+eng+comp
    percentage=(total/400.0)*100
    print name,"Your total marks is ",total," and percentage is:",percentage
    print "Do you want to enter more?'y/n'"
    a=raw_input("Enter your choice:")
    if(a=="n"):
        break

