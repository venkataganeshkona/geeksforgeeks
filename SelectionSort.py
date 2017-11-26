# Taking input from the system
input = map(int, raw_input().split(" "))
length = input[0]
posafter = input[1]
inputarray = map(int, raw_input().split(" "))

# Logical Code begins:

if (length == 0):
    print "Empty Array:"
elif (length == 1):
    print inputarray
else:
    for i in range(0, posafter):
        min = inputarray[i]

        temp = 0

        for j in range(i + 1, length):

            if (inputarray[j] < min):
                min = inputarray[j]
                minindex = j
                temp = inputarray[i]
                inputarray[i] = min
                inputarray[minindex] = temp

# Printing the array after x rotations
print(" ".join(str(x) for x in inputarray))



