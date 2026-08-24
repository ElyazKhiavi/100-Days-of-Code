# Data Overlap
# Instructions
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]

# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.


with open("./file1.txt", "r") as f:
    file1 = f.readlines()
    numbers1 = [int(i.replace('\n','').strip()) for i in file1]

with open("./file2.txt", "r") as f:
    file2 = f.readlines()
    numbers2 = [int(i.replace('\n','').strip()) for i in file2]

result = [i for i in numbers1 if i in numbers2]
print(result)