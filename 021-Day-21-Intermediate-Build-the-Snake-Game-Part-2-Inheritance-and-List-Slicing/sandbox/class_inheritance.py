class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, fname, lname, student_id, grade):
        super().__init__(fname, lname)      # pass the first/last name to Person
        self.student_id = student_id        # extra data only students have
        self.grade = grade

    def printname(self):
        super().printname()                 # print the Person part
        print(f"Student ID: {self.student_id} - Grade: {self.grade}")

    def __str__(self):
        return f"{super().__str__()} | ID: {self.student_id} | Grade: {self.grade}"


# Now create a Student with all required arguments
student1 = Student("Jane", "Smith", 12345, "A")
student1.printname()
print(student1)   # uses __str__




# ----------------------------------
# ----------------------------------

# !!!


class Animal:
    def __init__(self, name):
        self.name = name
        self.eyes = 2

    def breath(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def breath(self):
        super().breath()
        print("Underwater.")

    def swim(self):
        print("Swim in water")


my_fish = Fish("Nemo")
print(my_fish.eyes, my_fish.name)
my_fish.breath()
