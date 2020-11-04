class Cat:
    # class level variables defined
    flexibility = 10
    strength = 3

    # define purr function
    def purr(self):
        print("MEOOOW")

# Create 3 objects of cat, displaying attributes
becky = Cat()
print(f"becky: flexibility={becky.flexibility}, strength={becky.strength}")

brutus = Cat()
print(f"brutus: flexibility={brutus.flexibility}, strength={brutus.strength}")

karen = Cat()
print(f"karen: flexibility={karen.flexibility}, strenght={karen.strength}")

# Change attributes to suit cats
becky.flexibility = 20
brutus.strength = 18
brutus.flexibility = 4
karen.flexibility = 1

# Display new attributes
print(f"becky: flexibility={becky.flexibility}, strength={becky.strength}")
print(f"brutus: flexibility={brutus.flexibility}, strength={brutus.strength}")
print(f"karen: flexibility={karen.flexibility}, strenght={karen.strength}")
