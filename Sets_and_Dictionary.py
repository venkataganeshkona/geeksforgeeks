#Sets
a={"apple","mango","banana","apple","pear"}
print a
m=set('aabbbbcgddd')
n=set('ggbfddr')
print m-n
print m|n
print m&n
print m^n

a=(x for x in set('abracadabra') if x not in 'abc')
print a

#Dictionaries
dictionary={'jack':1000,'jake':2000,'robert':30000}
dictionary['benjamin']=4000
print dictionary

print sorted(list(dictionary.keys()));

print dict([('key1',100),('key2',200)])

