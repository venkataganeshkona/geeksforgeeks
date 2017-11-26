#Use case example of if and elif
print "Enter the number of classes held:"
n1=input()
print "Enter the number of classes attended:"
n2=input()
print "Did you have any medical issues?"
ans=raw_input()
percentage=(n2/float(n1))*100
print "Your attaendence percentage is:",percentage
if ((percentage>=75)):
    print "You are allowed to sit for the exam"
elif ((percentage<75) and ans=='Y'):
    print "You are allowed to sit for the exam"
else:
    print "You are not allowed to sit for the exams"