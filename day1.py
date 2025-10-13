

# input is used ta take the input from the user and its always in string format 
#  Ask user for their name
name = input("Enter your name: ")

# it will again return a string but we can convert it to int or float if needed 
# Ask user for their age
age = input("Enter your age: ")
age = int(age)  # Convert age to an integer


# Print the greeting using an f-string
print(f"Hello {name}, you are {age} years old")
# f-string is used to format the string and it is available in python 3.6 and above
# size 
import sys

a = 10
print(sys.getsizeof(a))   # size of integer

b = 10.5
print(sys.getsizeof(b))   # size of float

c = True
print(sys.getsizeof(c))   # size of bool

s = "Hello"
print(sys.getsizeof(s))   # size of string



# output:
# Enter your name: aditya singh 
# Enter your age: 19
# Hello aditya singh , you are 19 years old
# 28
# 24
# 28
# 54