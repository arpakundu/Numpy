import numpy as np
###broadcasting
a = np.tile(np.arange(0,40,10),(3,1))
print(a)
a = a.T ##transpose of array a
print(a)
b = np.array([0,1,2])
print(b)
print(a+b)
a = np.arange(0,40,10)
print(a)
print(a.shape)
a = a[:,np.newaxis] ##adds a new axis
print(a)
print(a+b)

print("*")
##flattening
a = np.array([[1,2,4],[4,1,6]])
print(a.ravel()) ##return a contiguous flattened array. A 1-D array containing the elements in the given order
print(a.T.ravel()) ##first transpose then flatten the array

print("*")
##reshaping
print(a)
print(a.shape)
b = a.ravel()
print(b)
print(b.shape)
b = b.reshape(2,3)
print(b)
print(b.shape)

print("*")
##numpy save the the normal and flattened array in the same location so changing the data in b changed the data in a automatically
b[0,0] = 100
print(a)

print("*")
#Note and beware: reshape may also return a copy and may not change the data of the given array
a = np.zeros((3,2))
b = a.T.reshape(3,2)
b[0,0] = 50
print(b)
print(a)

print("*")
###dimension suffling
a = np.arange(4*3*2).reshape(4,3,2)
print(a.shape)
print(a[0,2,1])

print("*")
##resizing
a = np.arange(4)
a.resize(8,)
print(a)
b = a
#print(a.resize(4,))   #this will give valueerror as another array is pointing to the same value so it cant be resized 

print("*")
#sorting data
a = np.array([[5,4,6],[2,3,2]])
b = np.sort(a,axis = 1)  ##sorting using another variable
print(b)
a = np.array([[5,4,6],[2,3,2]])
a.sort(axis=1) #in place sorting
print(a)
#sorting with fancy indexing
a = np.array([4,3,1,2])
j = np.argsort(a)
print(j) ##this returns the positions of indices after sorting
print(a[j]) ##now this will print the sorted elements
