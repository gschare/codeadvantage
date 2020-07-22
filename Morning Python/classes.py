class Animal:
    # The constructor
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def getWeight(self):
        return self.weight
    
    def getAge(self):
        return self.age

    def eat(self, amount):
        self.weight += amount

class Pet(Animal):
    isAnimal = True
    # Constructor
    # "overriding"
    def __init__(self, name, owner, age, weight):
        super().__init__(age, weight)
        self.name = name
        self.owner = owner

    def getName(self):
        return self.name

class Dog(Pet):
    def __init__(self, name, owner, breed, age, weight, sound):
        super().__init__(name, owner, age, weight)
        self.breed = breed
        self.sound = sound

    def getAge(self):
        return super().getAge()*7

    def bark(self):
        print(self.sound)

class Bunny(Pet):
    def __init__(self, name, owner, color, age, weight):
        super().__init__(name, owner, age, weight)
        self.color = color

    def getColor(self):
        return self.color

fido = Dog("fido", "john", "pitbull", 3, 80, "ruff!")
sierra = Dog("sierra", "gregory", "boxer", 4, 40, "roo!") # my dog!
apollo = Dog("apollo", "gregory", "terrier", 9, 20, "yap!") # my other dog!
hops = Bunny("hops", "lucas", "white", 1, 2)
pets = [fido, hops, sierra, apollo]

def feedPets(list_of_pets, amount):
    for pet in list_of_pets:
        print("=============")
        print(pet.getName().capitalize())
        print("Before:", pet.getWeight(), "lbs")
        pet.eat(amount)
        print("After:", pet.getWeight(), "lbs")

feedPets(pets, 5)

print("\n", sierra.getAge())
print(hops.getAge())
