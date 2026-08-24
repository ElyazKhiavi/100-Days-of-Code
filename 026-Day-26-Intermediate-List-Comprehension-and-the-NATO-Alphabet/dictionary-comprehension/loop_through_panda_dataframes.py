import pandas as pd

student_grades = {
    "student": [
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
    ],
    "grade": [81, 65, 38, 91, 52, 85, 47, 6, 50, 92],
}


df = pd.DataFrame(student_grades)
print(df)

for i in df.student:
    print(i)
for i in df.grade:
    print(i)

for index, row in df.iterrows():
    print(row.student)
