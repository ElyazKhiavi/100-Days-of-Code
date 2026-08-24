import random

students = [
    "Emma",
    "Liam",
    "Sophia",
    "Noah",
    "Olivia",
    "Mason",
    "Isabella",
    "Ethan",
    "Ava",
    "Logan",
]

student_grades = {name: random.randint(1, 100) for name in students}
passed_students = {
    name: grade for (name, grade) in student_grades.items() if grade >= 60
}
print(student_grades)
print(passed_students)
