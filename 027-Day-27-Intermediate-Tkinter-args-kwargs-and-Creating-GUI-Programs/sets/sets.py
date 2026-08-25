# Creating sets
s = {1, 2, 3}
t = set([3, 4, 5])

# Unique values only
nums = [1, 2, 2, 3]
unique_nums = set(nums)     # {1, 2, 3}

# Fast membership
if 2 in unique_nums:
    print("Yes")

# Operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # union: {1,2,3,4,5}
a & b   # intersection: {3}
a - b   # difference: {1,2}


