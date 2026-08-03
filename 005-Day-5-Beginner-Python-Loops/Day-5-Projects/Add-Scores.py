score = 0
student_scores = [
    100,
    171,
    98,
    134,
    189,
    130,
    199,
    84,
    174,
    110,
    195,
    119,
    116,
    110,
    192,
    121,
    90,
    105,
    188,
    106,
]
# for i in student_scores:
#     score+=i
# Simpler with sum()
score = sum(student_scores)
print(f"Total Score: {score}", f"\nScore avg: {round(score/(len(student_scores)+1),2)}")

print(max(student_scores),"max()")
print(min(student_scores), "min()")

        