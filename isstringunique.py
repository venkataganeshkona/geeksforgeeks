#IsStringUnique
S="ebcda";
A=sorted(S)
print A
is_duplicate=0
#Sorting the string
for i in range (0,len(A)-1):
    if(A[i]==A[i+1]):
        is_duplicate=1
        break
    else:
        continue

print is_duplicate


