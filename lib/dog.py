class Dog:
    # to have a default value for the less importatn attributes
    def __init__(self, name, breed="Mutt", fave_toy="Any"):
        self.name = name
        self.fave_toy = fave_toy
        self.breed = breed

    def bark(self):
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name  # our instance now has an owner attribute that we can access thru the self.owner
        # return self.owner


fido = Dog("Fido")  # Fido is born!
fido.get_adopted("Sophie")
print(fido.__dict__)
# Sophie
print(fido.owner)
# do not pass a value for the fave_toy
print(f"fave_toy: {fido.fave_toy}")

print("---------------------")
snoopy = Dog("Fido", "Tennis Ball")  # Fido is born!
print(snoopy.get_adopted("Ahmed"))
# Sophie
# pass a value for the fave_toy
print(f"fave_toy: {snoopy.fave_toy}")
