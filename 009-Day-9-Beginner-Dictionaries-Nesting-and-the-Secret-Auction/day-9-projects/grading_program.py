# Grading Program
# Instructions

# You have access to a database of student_scores in the format of a dictionary.
# The rkeys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.

# The final version of the student_grades dictionary will be checked.


student_scores = {
    "Emma Johnson": 92,
    "Liam Martinez": 78,
    "Sophia Chen": 88,
    "Noah Williams": 65,
    "Olivia Brown": 95,
    "Mason Davis": 34,
    "Isabella Garcia": 81,
    "Ethan Wilson": 73,
    "Ava Rodriguez": 100,
    "Logan Anderson": 59,
    "Mia Thompson": 67,
    "Lucas White": 43,
    "Charlotte Harris": 90,
    "Benjamin Lewis": 52,
    "Amelia Clark": 76,
}

student_grades = {}

# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

for i in student_scores:
    if 91 <= student_scores[i]:
        student_grades[i] = "Outstanding"
    elif 81 <= student_scores[i]:
        student_grades[i] = "Exceeds Expectations"
    elif 71 <= student_scores[i]:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"


for i in student_grades:
    print(f"{i}: {student_grades[i]} - {student_scores[i]}")


grades_avg = round(
    sum(student_scores.values()) / len(student_scores), 2
)  # adds all the numbers
max_grade = winner = max(student_scores, key=student_scores.get)
min_grade = winner = min(student_scores, key=student_scores.get)
print(max_grade, min_grade, grades_avg)
