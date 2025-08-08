import numpy as np
a=np.array([1,2,3,4])
print(a+1)
print(a**2)
b = np.ones(4) + 1
print(a-b)
print(a*b)

#matrix multiplication
c = np.diag([1,2,3,4])
print(c)
print("")
print(c*c)

#comparision operation
a=np.array([1,2,3,4])
b=np.array([5,2,2,4])
print(a==b)
print(a>b)

##arraywise comparisions
a=np.array([1,2,3,4])
b=np.array([5,2,2,4])
c=np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))

a=np.array([1,1,0,0],dtype=bool)
b=np.array([1,0,1,0],dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

##sine operation
a=np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

#mathematical operations with built in functions
####Reductions####
a=np.array([1,2,3,4,5])
print(np.sum(a))

x = np.array([[1,1],[2,2]])
print(x.sum(axis=0))  ##sum of the numbers of each column(collumnwise sum)
print(x.sum(axis=1))  ##sum of the numbers of each row(rowwise sum)

##printing the minimum element
print(a.min())
##printing the maximum element
print(a.max())
##printing the index of minimum element
print(a.argmin())
##printing the index of maximum element
print(a.argmax())

##Logical operations##
print(np.all(a)) #returns true if all elements are true/returns false if any of them are false(kind of logical and)
print(np.all([True,False,True]))
print(np.any(a)) #returns true if any of the elements are true/returns false if all of them are false(kind of logical or)
print(np.any([True,False,True]))
print(np.any([False,False,False]))

a = np.zeros((50,50))
print(np.any(a!=0))
print(np.all(a==a))

a=np.array([1,2,3,2])
b=np.array([2,2,3,2])
c=np.array([6,4,4,5])
print(((a<=b)&(b<=c)).all())

##statistics
x = np.array([1,2,3,4])
print(np.mean(x))
print(np.median(x))
y = np.array([[1,2,3],[5,6,1]])
print(np.median(y,axis=-1))
print(x.std())
