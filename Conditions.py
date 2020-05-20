# boolean conditions
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

print("\n")

# the "in" operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# python uses indentation to define code blocks instead of brackets.
# the standard indentation is 4 spaces, although tabs and any other
# space size works as long as consistent

# example of code blocks using "if" statements
# pass is a null statement (i.e. does nothing, to be implemented later)
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# example
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# a statement is evaluated as true under 2 conditions:
# 1.The "True" boolean variable is given, or calculated using
# an expression, such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.

# examples of objects considered "empty"
# 1. An empty string: ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

# the "is" operator
# Unlike the double equals operator "==", the "is" operator does not
# match the values of the variables, but the instances themselves.
# For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# the "not" operator
# Using "not" before a boolean expression inverts it:
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# EXERCISE
# change this code so that each "if" statement prints true
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")