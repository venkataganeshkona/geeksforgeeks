#This code takes a string and stores it in a hash table:
#s='ABCDE'
#While storing elements in a hash table,the time complexity is O(n),
#but while accessing the elements,the complexity is O(1)


def is_String_Unique(s):
    list_of_chars = list(s)
    length_of_string = len(list_of_chars)
    table_size=length_of_string
    sum=0
    #Implement the Hash Table
    hash_table=[None]*150
    flag=0
    for i in range(len(s)):
        if(hash_table[ord(s[i])]==s[i]):
            print 'Duplicate Characters !'
            flag=1
            break
        else:
            hash_table[ord(s[i])]=s[i]
    if(flag==0):
        print "No Duplicate Characters"



is_String_Unique('ABCDFFA')
