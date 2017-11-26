#This code checks if the given string is a permutation of the other string
S1='ABCDE'
S2='BADCE'

length_of_string=len(S1)
table_size=150
hash_table=[0]*150
#print hash_table

#Inserting the counts of the chars in a Hash Table
for i in range(length_of_string):
    index=ord(S1[i])
    count_at_index=hash_table[index]
    hash_table[index]=count_at_index+1

#Now checking the second string

flag = 0
for i in range(length_of_string-1):
    count = 1

    for j in range (i+1,length_of_string):
        if S2[i]==S2[j]:
            count=count+1
    index=ord(S2[i])
    if (hash_table[index]==count):
        continue
    else:
        flag=1
        break
if(flag==1):
    print 'Not a Permutation of the String'
else:
    print 'Permutation of the String'





