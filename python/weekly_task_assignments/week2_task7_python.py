# Function with Default Argument
# Question:
# Create a function greet(name, message="Welcome!") that prints:
# "Hello, <name>! <message>"
# •	Call the function with and without the message argument.

def greet(name, messsage="Welcome!"):
    print(f"Hello, {name}! {messsage}")

# Calling without a message argument

greet("ram")
    
# Calling with message argument

greet("ram", "How was your day?")

# Function with args (Variable Number of Arguments)
# Question:
# Create a function total(*numbers) that takes any number of numeric arguments and returns their sum.
# •	Example call: total(5, 10, 15) should return 30.

def total(*numbers):
    return(sum(numbers))
print(total(10, 30, 10))
print(total(60,40))
print(total(5, 10, 20, 25, 57))
print(total())

# Function with kwargs (Keyword Arguments)
# Question:
# Create a function display_info(**details) that prints key-value pairs like:
# name: Rajesh 
# age: 25  
# city: Kathmandu  

def display_info(**details):
    print(details)
display_info(name="Rajesh", age=25, city="Kathmandu")

# Function Using Both args and a Default Argument
# Question:
# Create a function repeat_words(*words, times=2) that repeats each word the given number of times.
# •	Example: repeat_words("Hi", "Bye", times=3)
# Output:

def repeat_words(*words, times=2):
    for word in words:
        print(word*times)
repeat_words("Hi", "Bye", times=3)




