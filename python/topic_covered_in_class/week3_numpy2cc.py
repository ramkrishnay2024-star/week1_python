# Bollean Indexing
# we give the condition its either True or Flase

import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
mod = 8%4 == 0
print(mod)
import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])
work = [1,2,3,4,5,6,7,8,9,10] % 2 == 0 
'''
Out put will show error
'''
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
work = array1 % 2 != 0
print(work)

array2 = np.array([1,2,3,4,5,6,7,8,9,10])
work = array2[array2 %2 == 0]
print(work)

array3 = np.array([1,2,3,4,5,6,7,8,9,10]) ###
equal_one = array3[array3 % 5 == 1]
print(equal_one)

l1 = [1, 2]
l2 = [3, 4]
print(l1 + l2)

l1 = np.array([1,2])
l2 = np.array([3,4])
print(l1 + l2)

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
print(numbers)
print(numbers[numbers%2==0])

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
numbers[numbers %2 != 0] = -100
print(numbers)

# Note: age are never in negative
age = np.array([2,-1,-100,-200,45,56,-33,33,0,0])
age[age<0] = 0
print(age)

age = np.array([2,-1,-100,-200,45,56,-33,33,0,0])
result = age<0
print(result)

age = np.array([2,-1,-100,-200,45,56,-33,33,0,0])
result = age[age>0]
print(result)

## Fancy Indexing

fancy = np.array([1,12,15,67,8,90])
print(fancy)

# Select elements
elements = fancy[[1,3,-1]]
print(elements)

r = np.array([100,444,213,786,546,999,1000,543,254,986])
print(type(r))
print(r[-2])
print(r[[-3,2,-1]])

a = np.array([2,4,6,8,9])
slices = a[-2:]
print(slices)

numbers = np.array([2,4,6,8,9,12,14])
print("Number of dimensions:",numbers.ndim)
printfirst = np.array([1,2,3,4,5,6])
second = np.array([9,8,7,6,5,4,3,2])
print(first.size)
print(second.size)

array1 = np.array([9,8,5,4,3,2,7,7])
array2 = np.array([6,7,8,9,10,11])     
array3 = np.array([1.2,2.4,5.6,7.8])    
print(array1)
print(array2)
print(array3)

print(array1.itemsize)
print(array2.itemsize)
print(array3.itemsize)('Shape:',numbers.shape)

number1 = np.array([1,2,3,7.8])
print(number1)
print("Data Type of First Array:",number1.dtype)
print(number1.nbytes)

first = np.array([1,5,5,7])
second = np.array([2,3,6,8])
sum = first + second
print(sum)

first = np.array([1,5,5,7])
second = np.array([2,3,6,8])
sum1 = np.add(first,second)
print(sum1)

first = np.array([3,9,27,81])
second = np.array([3,3,3,3])
result = first/second
print(result)
print(type(first[-1]))

import numpy as np
Warning('ignore')
ary1 = np.array([2,8,16,32])
ary2 = np.array([0,4,0,8])
result = np.divide(ary1,ary2)
print(result)

# 2. Comparison operator

first_array = np.array([1,2,3,4])
second_array = np.array([4,2,3,1])
comparision_1_2 = first_array != second_array
print(comparision_1_2)

a = np.array([1,2,3,4])
b = np.array([4,2,3,1])
comparision_1_2 = np.greater_equal(a,b)
print(comparision_1_2)

# 3. Logical Operator
'''
Logical AND
print(np.logic_and(x1,x2))

Logical OR
print(np.logical_or())

Logical NOT
print(np.logical_not(x1)) print(np.logical_not(x2))

'''

x1 = np.array([True,False,True,False])
x2 = np.array([False,False,True,True])
ands = np.logical_and(x1,x2)
ors = np.logical_or(x1,x2)
nots = np.logical_not(x1,x2)
print(ands)
print(ors)
print(nots)

# 4. Statistical Functions

import numpy as np

marks = np.array([97,77,93,81,85,83])
mean_marks = np.mean(marks)
print(mean_marks)
print(type(mean_marks))

# Meadian

arr1 = np.array([5,4,2,1,3,6])
median = np.median(arr1)
print(median)

arr2 = np.array([5,4,3,1,2,10,11])
print(np.mean(arr2))
print(np.median(arr2))

# Standard Deviation

marks = np.array([82,84,87,80,79,86])  ## Less Volatile
result = np.std(marks)
print(result)

marks = np.array([82,87,1,79,86])  ## Highly Volatile
print(np.std(marks)) 

array1 = np.arange(1,1000,3)
print(array1)
result1 = np.percentile(array1,50)
print("0th percentile:",result1)
print("Minimun Value:",min(array1))
print("median:",np.median(array1))
print("median:",np.mean(array1))

array1 = np.array([2,6,9,16,27,57,99])
minss_value = np.min(array1)
max_value = np.max(array1)
print("Minimun value:",minss_value)
print("Maximum value:",max_value)

## Creat 2d array

array1 = np.array([[1,2,3,4], [7,5,4,3]])
print(array1.ndim)

# ## Creat 3d array

array1 = np.array([[[1,2,3,4], [7,5,4,3]]])
print(array1.ndim)

array1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(array1)

lst1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(lst1)
np_array = np.array(lst1)
print(np_array)

## 2d array of inhomogenous shape

array1 = np.array([[1,2,3], [4,5,6], [7,8]])
print(array1)
'''
This will throw an error because of
irregular size inside the list bracket
'''

array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array1)

'''
This is the correct one!
It has the same size.
'''
# 2d array of different data types

array1 = np.array([[1,2,3], ['a','b','c'], [4.2,5.7,6.8]])
print(array1)
print(type(array1[0][0]))

# create a 3d array with 2 'slices' of 3 rows and columns each

np_array = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]], [[13,14,15,16], [17,18,19,20],
                       [21,22,23,24]]])
print(np_array)

# Create an ampty 2-D array with 2d rows and 3 columns

array1 = np.empty((2,3))
print(array1)

Create an empty 

array2 = np.empty((3,3,3))
print(array2)

print(np.empty((5)))

numpy_array = np.zeros((2,3))
print(numpy_array)

# Create a 2*3*4 array filled with 1s

numpy_array =np.ones((5,3,4)) # First value is block, second is rows and third is column
print(numpy_array)

# Numpy 'np.full' function

array1 = np.full((2,3), 111)
print(array1)

'''
or
'''
array1 = np.full(shape=(2,3), fill_value=111)
print(array1)

# 3D

array_3d = np.full((2,3,5),8)
print(array_3d)
print(array_3d[0][1][0])

# 4D

array_4d = np.full((2,3,2,3),7)
print(array_4d)
print("Array Dimension:",array_4d.ndim)
print("\nshape of the array:",array_4d.shape)

# Cheking the index
array1 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]],
    [[9,10],[11,12]]])
print(array1)

array2 = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(array2)

array1 = np.arange(1,11)
print(array1)
'''
Changing this
1D data to 2d
'''
result = np.arange(1,11).reshape(2,5)
print(result)  

array2 = np.arange(1,9)
result = np.arange(1,9).reshape(2,2,2)   
print(result)   

# Creat a 3D array:

array1 = np.arange(1,13).reshape(3,2,2)
print(array1) 
entire_array = array1[2:,:,:]
print(entire_array)
second_row_each_matrix = array1[:,:,0]
print(second_row_each_matrix)

# Change data:

np_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
(np_array)[1,1] = 99
np_array[2,0] = 88
print(np_array)

# Reshape the array 

array1 = np.array([1,2,3,4,5,6,7,8])
result = np.reshape(array1,(2,4))
print(result)

array1 = np.array([1,2,3,4,5,6,7,8])
result = np.reshape(array1, (2,4),order="C")
print(result)

array1 = np.array([1,2,3,4,5,6,7,8])
result = np.reshape(array1,(2,4),order='F')
print(result)





        
                  












