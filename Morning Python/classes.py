class Animal:
    age = 0
    weight = 0
    
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
    name = ""
    owner = ""
    age = 0
    weight = 0

    def __init__(self, name, owner, age, weight):
        super().__init__(age, weight)
        self.name = name
        self.owner = owner

    def getName(self):
        return self.name

class Dog(Pet):
    name = ""
    owner = ""
    breed = ""
    age = 0
    weight = 0

    def __init__(self, name, owner, breed, age, weight):
        super().__init__(name, owner, age, weight)
        self.breed = breed

    def getDogYears(self):
        return self.age*7

class Bunny(Pet):
    name = ""
    owner = ""
    color = ""
    age = 0
    weight = 0

    def __init__(self, name, owner, color, age, weight):
        super().__init__(name, owner, age, weight)
        self.color = color

    def getColor(self):
        return self.color

fido = Dog("fido", "john", "pitbull", 3, 80)
sierra = Dog("sierra", "gregory", "boxer", 4, 40) # my dog!
apollo = Dog("apollo", "gregory", "terrier", 9, 20) # my other dog!
hops = Bunny("hops", "lucas", "white", 0, 2)
pets = [fido, hops, sierra, apollo]

def feedPets(list_of_pets, amount):
    for pet in list_of_pets:
        print("=============")
        print(pet.getName().capitalize())
        print("Before:", pet.getWeight(), "lbs")
        pet.eat(amount)
        print("After:", pet.getWeight(), "lbs")

feedPets(pets, 5)
