# recreating max()
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

print(max(student_scores))

hold = student_scores[0]
for i in student_scores:
    if i > hold:
        hold = i
print(hold)
# print(student_scores.index(106),len(student_scores))



# recreating min()

print(min(student_scores))

for i in student_scores:
    if i<hold:
        hold =i
print(hold)