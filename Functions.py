# how to write functions
# python makes use of blocks
# ex:

# block_head:
#   1st block line
#   2nd block line
#   ...

# where block line is more code
# and block head is of format block_keyword block_name(parameter1, parameter2, ...)
# block keywords such as "if", "for", and "while"
# functions in python defined with keyword "def" and function name
# ex:
def my_function():
    print("Hello From My Function!")


# functions may also recieve arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


# functions may return value to caller
def sum_two_numbers(a, b):
    return a + b


# example
# using three functions declared above

# print(a simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1, 2)

# EXERCISE
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"
    pass

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()