# Python is a completely object oriented language and "statically typed",
# You dont need to declare variables before using them or declare a their type
#  Every variable in python is an object


# Numbers
# --------
# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals) (also complex)

# Defining integer
myint = 7
# or
myint = int(7)

# Defining floating point number
myfloat = 10.0
# or
myfloat = float(7)

# Division (/) always returns a float.

# To do floor division and get an integer result (discarding any fractional result) you can use the // operator; 
# to calculate the remainder you can use %:
print(7 // 5) # 1
print(7 % 5) # 2

# it is possible to use the ** operator to calculate powers 
5 ** 2 # 25


# Strings
# -------
# Strings are definied with single quote or double quotes
# Double quotes makes it easy to include apostrophes
mystring = "Don't worry about the apostrophes"
mysinglequotestring = 'Don\'t worry about the apostrophes'

# If you don’t want characters prefaced by \ to be interpreted as special characters, 
# you can use raw strings by adding an r before the first quote:
print(r'C:\some\name')

# String literals can span multiple lines. 
# One way is using triple-quotes: """...""" or '''...'''. 
# End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. 
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'inn') # unununinn

# Strings can be indexed (subscripted), with the first character having index 0.
word = "Python"
word[0] # P
word[5] # n
word[-1]  # last character

# While indexing is used to obtain individual characters, slicing allows you to obtain substring:
word[0:3] # Pyt

# Python strings cannot be changed — they are immutable. 
# Therefore, assigning to an indexed position in the string results in an error:
word[0] = 'J' # TypeError: 'str' object does not support item assignment

# If you need a different string, you should create a new one:
'J' + word[1:] # Jython

# The built-in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
len(s) # 34