# Numpy pratice

marks = [10, 20, 30, 40]
new_marks = []
for mark in marks:
    new_marks.append(mark+5)
print(new_marks)

import numpy as np

marks = np.array([10, 20, 30, 40])
print(marks**2)
print(type(marks))

import numpy as np

v = np.array([1,2,3])
print(type(v))

array4 = np.array([2,3,4,5,6])
print(array4)
print(type(array4))

# from numpy import array
a = array = ([1,2,3])
print(a)

import numpy as np

array2 = np.array((1,2,4))
print(array2)
print(type(array2))

my_list = [1,2,3]
print(my_list * 3)

double = [x *2 for x in my_list]
print(double)

# I wnt to do using array x*2:

import numpy as np

a = np.array([1,2,3])
mul = a*2
print(mul)

# Creat using numbers
import numpy as np

number = [1,2,3,4,54]
nparray = np.array(number)
print(nparray)
print(type(nparray))

#Tuple is converted to numpy array and outup came in oist stracture

import numpy as np
lsits = (1,2,3,4)
nparray = np.array(lsits)
print(nparray)

nums = {1,2,3,3,2,1}
print(np.array(nums))
print(type(np.array(nums)))

# creat an array with 10 elements filled with zeros

import numpy as np
array1 = np.ones(10)
print(len(array1))
print(array1)
print(type(array1))
print(type(array1[5]))

range function
lsts = []
lsts.extend(list(range(4)))
print(lsts)

lst = []
lst.extend(list(range(4,10)))
print(lst)

lst = []
lst.extend(list(range(2,25,2)))
print(lst)

array1 = range(10,20)
print(list(array1))

arrays = range(3, 20)
print(list(arrays))

arrays2 = range(3,20,3)
print(list(arrays2))

# array3 = range(3,20,2.3) # we can't put float in range. we can only put in arange
# print(list(array3))

import numpy as np
arrays4 = np.arange(3,20,2.3)
print(arrays4)

import numpy as np
lst = np.linspace(1,30)
print(lst)

import numpy as np
array5 = np.linspace(1,30)
print(array5)

lst = list(range(4))
print(lst)

lst = list(range(1,10))
print(lst)

lst = list(range(2,25,2))
print(lst)

import numpy as np
array1 = np.arange(10)
print(array1)

array2 = np.arange(3,50,2.7)
print(array2)

import numpy as np
print(np.linspace(1,100,3))

array2 = np.random.randint(1,81,7)
print(array2)

# Also we can put value like this:
rand_array = np.random.randint(high=81,low=1,size=10)
print(rand_array)

array2 = np.random.rand(10000)
print(array2)

## Without numpy

lst = [1,3,5,7,9,10]
lst1 =[]
for ls in lst:
    lst1.append(ls**2)
print(lst1)

lst=[]
for i in lst:
    lst.extend(list(range(1,10)))
    print(lst)

lst = []

for i in lst:
    print(i)
    lst.extend(range(1, 4))

l = [1,2,3,4,5]
l1 = []
for i in l:
    l1.append(i**2)
print(l1)

import numpy as np
print(np.empty(6))

import numpy as np
empty_array = np.empty(9)
print("Empty Array:",empty_array)

arr = np.array([1,2,3,4])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

try:
    print(arr[5])
except IndexError as a:
    print("The error is",a)