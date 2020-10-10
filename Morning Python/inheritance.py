class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def getInfo(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Nationality:", self.nationality)

    def giveDetention(self):
        print("You can't give this person detention because",
              self.name, "is not a student.")

class Student(Person):
    num_detentions = 0
    grade = 0
    favorite_class = ""
    
    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)

    def setGrade(self, grade):
        self.grade = grade
        
    def setFavoriteClass(self, favorite_class):
        self.favorite_class = favorite_class

    def getInfo(self):
        #super().getInfo()
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Favorite class:", self.favorite_class)

    def giveDetention(self):
        self.num_detentions += 1

principal = Person("Edward Rooney", 100, "American")    
Student1 = Student("Gregory Schare", 19, "American")
Student3 = Student("Ferris Bueller", 18, "American")
