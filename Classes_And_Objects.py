# a very basic class would look something like this:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# to assign the above class(template) to an object you would do the following:
myobjectx = MyClass()

# now the variable "myobjectx" contains the object of the class "MyClass" that contains
# the variable "variable" and the function "function" defined within "MyClass"

# to access object variable
myobjectx.variable

# ex:
print(myobjectx.variable)

# each object has an independent copy of the class, and can be edited independently
myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjecty.variable)

# accessing function inside an object
myobjectx.function()


# EXERCISE
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
