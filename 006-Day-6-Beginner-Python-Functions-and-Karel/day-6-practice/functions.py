# Functions
from random import randint
## defining a function
def my_function():
    print('Running the Function')

# my_function() # print  -> Running the Function


def func(arg):
    for _ in range(arg):
        print(randint(1,100000))

func(10) # print random numbers between the range in randint