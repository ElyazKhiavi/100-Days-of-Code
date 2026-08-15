import random
# 
data = {
    "1": {"name": "Alice", "age": 25, "city": "New York", "score": 85},
    "2": {"name": "Bob", "age": 30, "city": "London", "score": 92},
    "3": {"name": "Charlie", "age": 22, "city": "Paris", "score": 78},
    "4": {"name": "Diana", "age": 28, "city": "Berlin", "score": 88},
    "5": {"name": "Eve", "age": 35, "city": "Madrid", "score": 91},
    "6": {"name": "Frank", "age": 27, "city": "Rome", "score": 76},
    "7": {"name": "Grace", "age": 32, "city": "Tokyo", "score": 94},
    "8": {"name": "Henry", "age": 29, "city": "Sydney", "score": 83},
    "9": {"name": "Ivy", "age": 24, "city": "Toronto", "score": 79},
    "10": {"name": "Jack", "age": 31, "city": "Moscow", "score": 87},
}
# print(data[random.choice(list(data.keys()))]['name'])


for key in data:
    print(key, data[key]["name"])

    
class Student:
    """docstring for ClassName."""
    def __init__(self, name, age):
      self.name = name
      self.age = age
      self.grades = []
    
    def add_grade(self,grade):
        self.grades.append(grade)
