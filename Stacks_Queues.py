#Implementing Stacks and Queues in Python
stack=[1,2,3,4,5,6]
stack.append(7)
print stack
print stack.pop()
print stack

from collections import deque

queue=deque(["Apple","John","Kolkata"])
print  queue
queue.append("Ball")
print queue
queue.popleft()
print queue

#List Comprehensions
squares=[x**2 for x in range(10)]
print squares

#List Tuples
tuples=[(x,y) for x in range(1,10) for y in range(9,15) if x!=y]
print tuples


#More List Examples
vector=[0,1,2,3,4]
print vector
print [x**2 for x in vector]
print [(x,x**2) for x in vector]

#List Flatenning
vector=[[1,2,3],[4,5,6],[7,8,9]]
print [num for elem in vector for num in elem ]


#transpose a matrix
matrix=[[1,2,3,4],[4,5,6,7],[8,9,10,11]]
print matrix

#Listcomp
print [ [row[i] for row in matrix] for i in range(4)]

del(matrix[1])
print matrix

#Lists are mutable and tuples are immutable
t="Harry","jerry","Jack"
u=[1,2,3]
z=u,t
print z #tuples




