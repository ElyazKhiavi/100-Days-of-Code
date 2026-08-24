# list-comprehension

# with list
x = [1, 2, 3, 4, 5]
x_plus = [i + 1 for i in x]  # This is list comprehension
print(x_plus)

# with range
x = [i for i in range(10)]  # this is also valid
print(x)

x = [i for i in range(15, 0, -1)]  # !!!
print(x)


## want [2,4,6,8]

nums = [i for i in range(2,9,2)] # ==> [2, 4, 6, 8]
x = [i*2 for i in range(1,5)] # ==> [2, 4, 6, 8]


# with string
my_name = "Dante"
letters = [l for l in my_name]
print(letters)


# with numbers!
my_num = 123456
nums = [int(n) for n in str(my_num)]
print(nums)


