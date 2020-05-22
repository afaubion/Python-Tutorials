# A Closure is a function object that remembers values in enclosing scopes
# even if they are not present in memory.
# Let us get to it step by step

# Firstly, a Nested Function is a function defined inside another function.
# It's very important to note that the nested functions can access the variables of the enclosing scope.
# However, at least in python, they are only readonly.
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
# Ex: -----
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))
# -----
# Output:
"""
Test message
None
"""

# This works well as the 'data_transmitter' function can access the 'message'.
# To demonstrate the use of the "nonlocal" keyword, consider this
# -----
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)
# -----
# Output:
"""
3
3
"""

# And we call the function as follows:
# -----
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
# -----
# Output:
"""
Burn the Sun!
"""

# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved.
# This technique by which the data is attached to some code even after end of those other original functions
# is called as closures in python

# ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.
# (Eg. When there are few methods in a class, use closures instead).

# Also, Decorators in Python make extensive use of closures.

# EXERCISE
# Make a nested loop and a python closure to make functions to get multiple multiplication
# functions using closures. That is using closures, one could make functions to create multiply_with_5()
# or multiply_with_4() functions using closures.
# -----
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
# -----
# Output:
"""
45
"""