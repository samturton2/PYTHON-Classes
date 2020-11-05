# classes, objects and instantion

# how to create a class
# Syntax: class name_of_class starting with Capital letter
# Good naming convention is required

# classes are a way to bring data and functionality together
class Dog:

    animal_kind = "canine"
    # defining class variable

    def __init__(self, name, colour): #initialising dog class
        self.name = name
        self.colour = colour

    # self refers to current class
    def bark(self):
        return "woof"

# In order to execute a class we have to create an object of this class
fido = Dog("lassie", "brown") # creating an object of dog class

print(fido.animal_kind)
print(fido.bark())
print(fido.colour)

# manually change attribute
fido.animal_kind = "big dog"
print(fido.animal_kind)
