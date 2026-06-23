# Integer and Float Mix
#  •	Create an integer a and a float b.
#  •	Perform addition, subtraction, multiplication, and division on them.
#  •	Print the results and observe the type of each result with type().


a = 150
b = 70.55
print("Addition: ", a+b, "Sub: ", a-b, "Mul: ", a*b, "Div: ", a/b)
print("Addition: ", type(a+b),"\n" "Subtraction: ",type(a-b), "\n" "Multiplication: ", type(a*b), "\n" "Division: ",type(a/b))

# Large Integers And Type

# •	Assign a very large integer to a variable (e.g., in the billions).
# •	Print it and confirm its type is still int in Python or not.


billions = 780000000000
print(type(billions))

# Complex Number Basics

# •	Create a complex number z = 3 + 4j.
# •	Print its real part, imaginary part, and confirm its type is complex.
# •	Perform a basic arithmetic operation with another complex number (e.g., (3 + 4j) + (1 + 2j)).


z = 3 + 4J
print("Real part:", z.real, "Imaginary part:", z.imag)
print(type(z))

a = 1+7j
b = 3+9j
result = a+b
print(result)

# Boolean from Comparisons
# •	Create two variables, m = 10 and n = 15.
# •	Define status = (m > n) and print status.
# •	Confirm type(status) is bool.
# •	Assign status = (m != n) and print again.


m = 10
n = 15
status = m>n
print(status)
print(type(status))
status = m != n
print(status)
print(type(status))

# String Creation and Indexing
# •	Create a string text = "HelloWorld".
# •	Print the first and last characters using positive and negative indexing.
# •	Comment on the total length of the string.


text = "HelloWorld"
print(text[0], text[-1], len(text), sep='\n')

# String Slicing
# •	With lang = "PythonProgramming", print the substring from index 2 to 8.
# •	Print the substring from the start up to index 5.
# •	Print the entire string in reverse using slicing.


lang = "PythonProgramming"
print(lang[2:9])
print(lang[:6])
print(lang[: : -1])

# String Methods: Strings are immutable(can't be changed) in Python.
# •	Let phrase = " Hello, Python World! ".
# •	Demonstrate strip(), upper(), and replace() on this string.
# •	Print the results and comment on immutability of strings in Python.

phrase = " Hello, Python World! "
stripped = phrase.strip()
upper_case = phrase.upper()
replaced = phrase.replace("World", "Developer")
print(phrase)
print(stripped)
print(upper_case)
print(replaced)

phrase = "Hello"
upper_case = phrase.upper()
print(upper_case)

# String Formatting
# •	Create two variables: name = "Rajesh" and score = 95.
# •	Print: "Alice scored 95 points." using two methods (concatenation and an f-string or str.format()).

name = "Rajesh"
score = 95
print(f"{name} scored {score} points.")

# Boolean Operations in Expressions
# •	Write a small expression using and, or, and not with boolean values.
# •	Example: result = not(True and False) or (5 > 3).
# •	Print result and explain how Python evaluated the expression.


exp = True and True and True and True
print(exp)
exp2 = False and True and True
print(exp2)

# In 'and' expression if everything is True then only the output is True else False

exp_or = False or False or False
print(exp_or)

exp_or2 = True or False or False
print(exp_or2)

# In 'or' expression if all the inputs are False then its False else its True.

exp_no = not True
print(exp_no)

# 'not' expression just gives the opposite output 

result = not(True and False) or (5>3)
print(result)

# (True and False) is False. So not False = True because not does opposite. And True or True is also True so output is True

# List Creation and Access
# •	Create a list of 5 different integers.
# •	Print the first item, middle item, and last item using indexing.

lst = [1,2,3,4,5]
print(lst[0], lst[2], lst[-1])

# List Insertion and Deletion
# •	Start with a list nums = [10, 20, 30, 40].
# •	Insert 25 at index 2.
# •	Remove the last element.
# •	Print the updated list.

nums = [10,20,30,40]
nums.insert(2, 25)
print(nums)
nums.remove(40)
print(nums)

nums = [10,20,30,40]
nums.insert(2, 25)
print(nums)
nums.pop(-1)
print(nums)

nums = [10,20,30,40]
nums.insert(2, 25)
print(nums)
del nums[-1]
print(nums)

# List Slicing
# •	Given letters = ["a", "b", "c", "d", "e"], print the slice that contains only ["b", "c", "d"].
# •	Print the slice that omits the first and the last element.

letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])

# Sorting and Reversing
# •	Create a list of random integers.
# •	Sort the list in ascending order and print it.
# •	Reverse the sorted list and print again.

numbers = [10, 30, 20, 40, 35]
numbers.sort()
print("Assending order:",numbers)
numbers.reverse()
print("Item Reversed:",numbers)

# Combining Lists
# •	Let list1 = [1, 2, 3] and list2 = [4, 5, 6].
# •	Combine them into a single list and print.
# •	Demonstrate two ways: using + and using .extend().

list1 = [1,2,3]
list2 = [4,5,6]
list_combined = list1 + list2
print(list_combined)

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list1.extend(list2)
list1.extend(list3)
print(list1)

# Aggregating List Values
# •	Create a list of floats, e.g., [2.5, 3.6, 1.2, 5.0].
# •	Print the sum, minimum, and maximum of that list using built-in functions.

num_flo = [2.5, 3.6, 1.2, 5.0]
print("Sum:", sum(num_flo))
print("Minimum:",min(num_flo))
print("Maximum:",max(num_flo))

# Tuple Creation. Tuple Indexing & Slicing
# •	Create a tuple t = (10, 20, "Hello", True).
# •	Print the tuple and confirm its type with type(t).

t = (10, 20, "Hello", True)
print(type(t))
print(t[:2])
print(t[-1])

# Tuple Unpacking
# •	Suppose t2 = ("Tom", 25, "Engineer").
# •	Unpack it into three separate variables: name, age, profession.
# •	Print these variables individually.

t2 = ("Tom", 25, "Engineer")
print("Name:",t2[0])
print("Age:",t2[1])
print("Profession:",t2[-1])

# Attempt Tuple Mutation
# •	Try to change an element of t (t[0] = 999) and observe the error.
# •	In comments, explain why the error occurs.

# t3 = ("ram", 1, True)
# t3[0] = 999
# print(t3)
''' 
Tuples are immutable their value can not be chaned once created!
'''

# Set Creation & Membership. Add and Remove Elements
# •	Create a set my_set = {1, 3, 5, 7}.
# •	Check if 5 is in my_set.
# •	Check if 2 is not in my_set.

# Add & Remove Elements
# •	Add 9 to my_set.
# •	Remove 3 from my_set.
# •	Print the updated set.


my_set = {1, 3, 5, 7}
print(5 in my_set)
print(2 not in my_set)
my_set.add(9)
my_set.remove(3)
print(my_set)

# Set Operations
# •	Create two sets: setA = {1, 2, 3} and setB = {3, 4, 5}.
# •	Print the union, intersection, and difference (setA - setB).

setA = {1,2,3}
setB = {3,4,5}
print("Union:",setA | setB)
print("Intersection:",setA & setB)
print("Difference:",setA - setB)
print("DifferenceB:",setB - setA)

# Checking Unique Values using set
# •	Define a list vals = [1, 2, 2, 3, 3, 3, 4].
# •	Convert it to a set.
# •	Print both the list and the set to show how duplicates are removed.

vals = [1,2,2,3,3,3,4] 
con_set = set(vals)
print("List:",vals)
print("Set:",con_set)

responses = ["Yes", "No", "Yes", "Maybe", "No"]

uniq_res = set(responses)

print(uniq_res)

# Frozenset Creation
# •	Create a frozenset from a list [2, 4, 4, 6].
# •	Print it and observe whether duplicates are preserved.

numbers = [2,4,4,6]
numbers.append("None")
fset = frozenset(numbers)
print(fset)

#Normal set(mutable: add, remove)

my_set = {1,2,3}
my_set.add(4)
my_set.remove(2)
print(my_set)

# Frozen set (Immutable)

# fset = frozenset([1,2,3])
# fset.add(4)
# fset.remove(2)
# print(fset)

# Operator Precedence
# •	Define a = 4, b = 2, c = 5.
# •	Print the result of a + b * c vs. (a + b) * c.
# •	Explain in comments how the result differs.

a = 4
b = 2
c = 5
print(a+b*c)
print((a+b)*c)

'''
In first print(a+b*c) it multiply and then add. Similarly, 
In the second print((a+b)*c) it's added first(value inside bracket) 
and then multiplyed so out put is different.
conclusion: Python also as rules like Bodmas.
'''

# Modulo & Floor Division
# •	Let x = 17 and y = 4.
# •	Print x % y and x // y.
# •	Explain the difference between these two operators in comments.

x = 17
y = 4
print("Modulo:",x%y)
print("Floor Division:",x//y)

'''
Modulo = Imagine we have 17 candy to distribute
and 1 is left over. So remainder is printed in modulo
Floor Divsion = Imagine with total 17 candy we can distribute 
4 candy to each group and one is left over. Whole is printed and decimal part
is removed.
'''

# Power Operator
# •	Print the result of 2 ** 3.
# •	Write a line to calculate 3 ** 4.
# •	Print the addition of both.

a = 2**3
b = 3**4
print("2**3:",a)
print("3**4:",b)

print("Addition of Both:",a+b)

# String Comparison
# •	Compare "apple" and "banana" with <, >, and ==.
# •	Print the results.

a = "apple"
b = "banana"
print(a>b)
print(a<b)
print(a==b)

'''
It compares alphabetically 'a' comes first than'b' 
so second comparision is 'True'
'''

# Mixed Type Comparision
# •	Compare 5 and 5.0 with ==.
# •	Compare 5 and 5.0 with is.
# •	Discuss the results in comment.

a = 5
b = 5.0
print(a==b)
print(a is b)

'''
== checks whether the values are equal. Since the value is same so its "True"
is checks wether both variables refer to the exact. It does not "False"
same object in memory.
'''

# Chain Comparision
# •	Evaluate the expression 2 < 3 < 5.
# •	Print the result and explain how Python handles chained comparisons.

result = 2<3<5
print(result)

'''
(2<3) and (3<5) True and True = True
'''

# Logical and
# •	Define p = True and q = False.
# •	Print p and q.
# •	Demonstrate a real-world example: (age > 18) and (has_ID == True).

p = True
q = False
print(p and q)

# Real World Example. If they are avobe 18 and has id they can enter the club

age = int(input("Enter the age:"))
has_ID = True

print(age>18) and (has_ID==True)

# Logical or
# •	Using the same p and q, print p or q.


p = True
q = False
print(p or q)

# or real world example

is_logged_in = True
is_admin = False

print(is_logged_in or is_admin)

is_member = False
is_paidfee = True
is_oranizations_familymembers = False
print(is_member or is_paidfee or is_oranizations_familymembers)

# Logical not
# •	Let r = (10 > 5).
# •	Print r, then print not r.

r = (10>5)
print(r)
print(not(r))

# Using len()
# •	Create a list with 7 elements.
# •	Use len() to get the total count.
# •	Print the result.

lst = [1, "apple", "True", 4, 5, 6, 7]
total_lst = len(lst)
print(total_lst)

# Using type()
# •	For each of the following: 10, 10.5, "ten", True, 3+2j, print type(...).
# •	Summarize in comments the data types you observed.

print(type(10))
print(type(10.5))
print(type("ten"))
print(type(True))
print(type(3+2j))

'''
Summary of data types
10 = int
10.5 = float
"ten" = str
True = bool
3+2j = complex
'''

# Using abs()
# •	Print abs(10), abs(-10), and abs(-3.5).
# •	Explain what abs() does in comments.

print(abs(10))
print(abs(-10))
print(abs(-3.5))
print(abs(0))

'''
abs stands for absolute value so it eliminates 
negative sign and shows output positive only.
'''

# Using round()
# •	Demonstrate round(3.14159, 2).
# •	Show how round(2.5) behaves in Python.

print(round(3.14159, 2))
print(round(2.5))
print(round(3.5))

'''
1st print 2 indicate only 2 decimal digit.
'''

# Using sum(), max(), min()
# •	Create a list of numeric values.
# •	Print sum(), max(), and min() of that list.

lst = [10,20,30,40]

print(f"""
Sum: {sum(lst)}
Max:{max(lst)}
Min:{min(lst)}
""")

# Using sorted()
# •	Create a list or tuple vals = (3, 1, 4, 2).
# •	Use sorted(vals) and print the result.
# •	Show that vals itself is unchanged.

vals = (3,1,4,2)
sorted_vals = sorted(vals)
print(sorted_vals)
print(vals)

# Using any()/all()
# •	Create a list of booleans, for example [True, False, True].
# •	Print any() on the list, then all() on the list.
# •	Show the difference in how they evaluate.

lst = [True, False, True]
print(any(lst))
print(all(lst))

'''
'any' is like 'or' if one value is True. The outcome is True.
'all' is like 'and' if allvalue is True. Then only it's True else False
'''

# Storing Booleans from Comparisons
# •	Compare two values in separate expressions, e.g., a = (10 > 3), b = (5 == 5).
# •	Combine these booleans with and or or.
# •	Print the final result.

a = (10>3)
b = (5==5)
print(a and b)
print(a or b)

# Multiline String & Counting
# •	Create a multiline string describing your favorite hobby.
# •	Use the string method .count(substring) to count how many times the letter "a" appears (case-insensitive).
# •	Print the count and explain any steps taken to handle case sensitivity.

hobby = """
I enjoy playing Cricket.
Circket helps me to stay active and fresh.
I love outdoor games.
"""
count_a = hobby.lower().count("a")
print("Number of 'a' count:",count_a)

'''
I have used .lower() method because python is case sensitive. 
And used count() method to count all 'a'.
'''

# Advanced String Slicing
# •	Take the string "ABCDEFGHIJ" and slice every second character, resulting in "ACEGI".
# •	Print the sliced string.
# •	Also slice in reverse step.

str = "ABCDEFGHIJ"
print(str[::2])
print(str[::-1])

# Casefold vs. Lower
# •	Create two strings, "Case" and "case".
# •	Compare them with the regular == operator directly.
# •	Compare them again after applying .casefold().
# •	Print results and comment on how .casefold() differs from .lower() in edge cases.

a = "Case"
b = "case"
print("Direcet Comparision:",a==b)
print("Case Fold Comp:",a.casefold()==b.casefold())

# Formatted Printing 
# •	Define name = "Ramesh", product = "Notebook", quantity = 2, and price = 12.50.
# •	Use an f-string (or str.format()) to print:
# "Ramesh purchased 2 Notebook for a total of $25.0."

name = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50
print(f"{name} purchased {quantity} {product} for a total of {price*2} ")

# Type Conversion chain
# •	Ask a user for a string that represents a number, e.g., "0".
# •	Convert it to a float, then to a bool, and print the intermediate and final results.

num_str = input("Enter a number:")
con_flt = float(num_str)
con_bool = bool(con_flt)

print("Orginal String:",num_str)
print("As Float:",con_flt)
print("As Bool:",con_bool)

# String List Sorting
# •	Given fruits = ["apple", "banana", "cherry"], sort them in descending alphabetical order.
# •	Print the sorted list, then use the .reverse() method to flip it. Compare the two results.

fruits = ["apple", "banana", "cherry"]
sorted_desc = sorted(fruits,reverse=True)
print("Decending Sort:",sorted_desc)
sorted_desc.reverse()
print("After reverse:",sorted_desc)

# Insert Using Slicing
# •	Start with a list [2, 5, 7, 1, 9].
# •	Insert the value 4 right after the 2 using slicing (not insert() or append()).
# •	Print the modified list.

lst = [2,5,7,1,9]
lst[1:1]=[4]
print(lst)

# Indexing Within a Mixed List
# •	Create a list info = ["John", 28, True, 4500.75].
# •	Print only "John" and 4500.75 using their indices.

info = ["John",28,True,4500.75]
print(info[0],info[-1])

# Tuple Concatenation and Replication
# •	Create two tuples (1, 2) and (3, 4).
# •	Concatenate them into (1, 2, 3, 4).
# •	Replicate (1, 2) 3 times to get (1, 2, 1, 2, 1, 2).

a = (1,2)
b = (3,4)
concat = a+b
print("Joined:", concat)
repeted = a*3
print("Repeted:",repeted)

# Single Element Tuple
# •	Demonstrate that (42,) is a tuple whereas (42) is just an integer.

a = (42,)
b = 42
print(type(a))
print(type(b))

# Intersection and Union
# •	Let setA = {1, 2, 3, 4} and setB = {1,2,3}.
# •	Print their intersection using setA & setB.
# •	Print their union using setA | setB.

setA = {1,2,3,4}
setB = {1,2,3}
print(setA&setB)
print(setA|setB)

# Subset and Superset
# •	Check if setB is a subset of setA using setB.issubset(setA).
# •	Check if setA is a superset of setB using setA.issuperset(setB).
# •	Print the results.


setA = {1,2,3,4,5}
setB = {2,3,4}
print("Is setB a subset of setA?",setB.issubset(setA))
print("Is setA a superset of setB?",setA.issuperset(setB))























































