#This code gives the example of writing on files
file=open("new","w") #opening the file in write mode
print file
file.write("This is the first line \n")
file.write("This is the second line.")
file.close()

#Second example
file=open("new","r") #opening the file in read mode
t=file.read()
print t
file.close()

#Thired example
file=open("new","r")
t=file.read(2)
print t
t=file.read(999)
print t
file.close()

