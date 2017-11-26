#This code explians the concept of dictionary
d={'mango':40,'apple':50,'cherry':60}
print d.keys()
print d.values()
print d['mango']
print d['cherry']
#-----------------------------------
new={'x':[1,2,3,4],'y':"Hello world",'z':4.0}
print new
#-----------------------------------
new1={60:'x',30:'y',40:'z',50:'m'}
for i in sorted(new1):
    print i,":",new1[i]
#-----------------------------------
new2={60:'x',30:'y',40:'z',50:'m'}
print new2.has_key(60)
print new2.has_key(70)