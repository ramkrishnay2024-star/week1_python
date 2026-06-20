# # Python Data Structures Assignments
# # Section 1 : List

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"Total numbers: {numbers} \n ")
favourite5_fruits = ['mango', 'apple', 'strawberry', 'avacado', 'orange']
print(f"My Five Favourite Fruits: {favourite5_fruits}")

# # Accessing Elements:

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1], '\n')
print(f"{numbers[0]} {numbers[-1]}")

# Creatin List Length

lst = ['cricket', 'basketball', 'hockey', 'swimming', 'boxing']
print(len(lst))

# Adding Element (appending)

lst = []
lst.extend([1,2,3])
print(lst)

lst = []
lst.append([1,2,3])
print(lst)

# Inserting an Element
# Insert(index, value)

lst = [1,3,4]
lst.insert(1, 2) 
print(lst)

# Removing an Element

lst = [1,2,3,4]
lst.remove(3)
print(lst)

# Popping an Element 

lst = [10,20,30,40]
lst.pop(-1)
print(lst)

# Slicing a List

lst = [0,1,2,3,4,5]
print(lst[2:5])

# List Concatenation

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_1_and2 = lst_1+lst_2
print(lst_1_and2)

# Repeating a List

lst = [1,2]
lstr = lst*3
print(lstr)

# Copying a List

lst = ['pen', 'copy', 'book', 'scale']
lst_copy = lst.copy()
lst_copy.append('table')
print("Orginal: ", lst)
print("Copy: ", lst_copy)

lst = ['pen', 'copy', 'book', 'scale']
lst_copy = lst
lst_copy.append('table')
print("Orginal: ", lst)
print("Copy: ", lst_copy)

'''
If we don't use .copy() new list will not be created
and both variables point to the same list in memory. when 
we apppend or change data it will be applied on both.
'''

# Clearing a List
lst = [1,2,3,4,5]
valua =lst.clear()
print(lst)

# Section 2: Tuples

digits = (1,2,3)
print("Numbers: ", digits, '\n')

color = ('red', 'green', 'black')
print("Colors: ", color)

# Accessing Tuple Elements

num = (10,20,30,40)
print(num[1])

# Tuple Slicing

num = (0, 1, 2, 3, 4)
print(num[1:4])

# Concatenation Tuples

num1 = (1,2)
num2 = (3,4)
num1_num2 = num1 + num2
print(num1_num2)

# Tuple Unpacking

name = ("Alice")
age = (25)
city = ("New York")
print(name)
print(age)
print(city)

person = ("Alice", 25, "New York")
name, age, city = person
print(name)
print(age)
print(city, "\n")
print(name, age, city)

# Convert List to Tuple:

lst = [1,2,3,4]
lst_convert = tuple(lst)
print(lst_convert)

# Counting Occurrences:

num = (1,2,2,3,2)
count_2 = num.count(2)
print(count_2)

# Finding Index

num = [10,20,30,40]
print(num[2])








