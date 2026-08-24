# Filtering Even Numbers
# Instructions
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   

# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 
# Again, try to use Python's List Comprehension instead of a Loop.  

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
result = [i for i in numbers if i % 2 == 0]

print(result)

## Simpler?

r = [i for i in [int(j) for j in list_of_strings] if i % 2 == 0]
print(r)