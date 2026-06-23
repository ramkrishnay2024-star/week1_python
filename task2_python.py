# Python Data Structures Assignment 
# Section 1: Lists
# 1.	Create a List:
# Create a list containing the numbers 1 through 15. Print the list.
# 2.	List of Strings:
# Create a list of your five favorite fruits. Print the list.
# 3.	Accessing Elements:
# Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.
# 4.	List Length:
# Create a list of any 5 items and print its length using the len() function.
# 5.	Appending Elements:
# Start with an empty list and append the numbers 1, 2, and 3. Print the list.
# 6.	Inserting an Element:
# Given a list [1, 3, 4], insert the number 2 at the correct position so that the list becomes [1, 2, 3, 4].
# 7.	Removing an Element:
# Remove the number 3 from the list [1, 2, 3, 4, 5] using a list method and print the new list.
# 8.	Popping an Element:
# Given the list [10, 20, 30, 40], pop the last element and print the element and the updated list.
# 9.	Slicing a List:
# Given the list [0, 1, 2, 3, 4, 5], print a slice that contains the elements from index 2 to 4.
# 10.	List Concatenation:
# Concatenate two lists, e.g., [1, 2, 3] and [4, 5, 6], and print the resulting list.
# 11.	Repeating a List:
# Create a list [1, 2] and print the list repeated three times.
# 12.	Copying a List:
# Create a copy of a given list and print both the original and the copy.
# 13.	Clearing a List:
# Given any list, use a method to clear all its elements and then print the empty list.




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
# 1.	Create a Tuple:
# Create a tuple containing the numbers 1, 2, and 3. Print the tuple.
# 2.	Tuple of Strings:
# Create a tuple of three different color names and print it.
# 3.	Accessing Tuple Elements:
# Given the tuple (10, 20, 30, 40), print the second element.
# 4.	Tuple Slicing:
# Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.
# 5.	Concatenating Tuples:
# Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result.
# 6.	Tuple Unpacking:
# Store the tuple ("Alice", 25, "New York") into three variables and print them.
# 7.	Convert List to Tuple:
# Convert the list [1, 2, 3, 4] into a tuple and print the tuple.
# 8.	Counting Occurrences:
# Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.
# 9.	Finding an Index:
# In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.



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








