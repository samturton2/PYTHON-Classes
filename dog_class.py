# classes, objects and instantion

# how to create a class
# Syntax: class name_of_class starting with Capital letter
# Good naming convention is required

# classes are a way to bring data and functionality together
class Dog:

    animal_kind = "canine"
    # defining class variable

    # self refers to current class
    def bark(self):
        return "woof"

# In order to execute a class we have to create an object of this class
fido = Dog() # creating an object of dog class

print(fido.animal_kind)
print(fido.bark())
fido.animal_kind = "big dog"
print(fido.animal_kind)

lassie = Dog() # creating an object of dog class
print(lassie.bark())
print(lassie.animal_kind)
