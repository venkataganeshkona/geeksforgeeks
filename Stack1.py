#Implementing a Stack using an array

def stack_using_array_push(array,a):
    rear=0
    top=len(array)-1
    array.append(a)
    top=top+1
    return top

def stack_using_array_pop(array):
    rear=0
    top=len(array)-1
    del(array[top])
    top=top-1
    return top

array=[1,2,3,4,5,6]
#top_elem=stack_using_array_push(array,7)
#print 'New Top after Push= ',top_elem
#print 'List after Push: ',array

top_elem=stack_using_array_pop(array)
print 'New Top after Pop= ',top_elem
print 'List after Pop: ',array



