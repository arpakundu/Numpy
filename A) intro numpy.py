###NUMPY###
import numpy as np
a = np.array([0,2,3,4,5]) ###making array with a list
print(a)

print(np.arange(20)) ####making an array with arange() within a specific range

# import timeit                ''''This only 
# L = range(50)                     works in
# %timeit [i**2 for i in L]        jupiter notebook''''

import timeit
L = range(50)
print(timeit.timeit("[i**2 for i in L]", globals=globals(), number=1000000))

# b = np.arange(1000)
# %timeit b**2

a = np.array([1,2,3,4]) #1-D Arry(vector) creation

a.ndim #print dimension

a.shape #print shape

len(a) #print length

b = np.array([[1,2,3,4],[5,6,7,8]]) #2-D Arry(matrix) creation

len(b) # print the size of the first dimension for example here 2(2 rows)

c = np.array([[[0,1],[2,3]],[[4,5],[6,7]]]) #3-D Arry(tensor)/n-D array creation

b = np.arange(20)
c = np.arange(1,20,5) # start, end, step

a = np.linspace(0,1,6) # start, end, nummber of points

# some common array creation syntax###
a = np.ones((3,3)) #The default data type is float ones and zeros function
b = np.zeros((3,3))
c = np.eye(3)
d = np.eye(3,2)
e = np.diag([1,2,3,4]) #creating diagonal array
print(np.diag(e)) # extracting the diagonal
print(f"{a}\n{b}\n{c}\n{d}\n{e}")

## creating array with random number
a = np.random.rand(4) #for uniform number
b = np.random.randn(4) # for standared number

#finding data type
print(a.dtype)

#changing data type
a = np.arange(10, dtype='float64')  # initially it was in int and now after declaring it as float it got changed

#some othe data types array
d = np.array([1+2j],[2+4j])
b = np.array([True,False,True])
s = np..array(['Ram','Shyam','Jodu','Madhu'])

#indexing in array
a = np.arange(10)
print(a[5])

a=np.diag([1,2,3,4])
print(a[2,2])

#assigning value
a[2,1] = 5

#slicing in array
a[1:8:2] 

#combine assignment and slicing
a[5:] = 10
a[5:] = b[::-1]

##copies and views
a = np.arange(10)
b = a[::2]
np.shares_memory(a,b) ##true
b[0] = 10
print(a) # a also got modified because of memory sharing
a = np.arange(10)
c = a[::2].copy()
np.shares_memory(a,c)  ##now its false because its copying data not sharing memory
c[0] = 10
print(a) # a didn't get modified

###false indexing
a = np.random.randint(0,20,15) ##here 0 is start, 20 is end and we need total 15 numbers
mask = (a%2==0)
extract_from_a = a[mask]
a[mask] = -1 ###converts all the number in the mask into -1
