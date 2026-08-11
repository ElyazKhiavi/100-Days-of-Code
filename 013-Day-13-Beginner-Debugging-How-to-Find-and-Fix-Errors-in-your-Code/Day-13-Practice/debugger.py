from readline import write_history_file
from random import random
import random


def change_number(nums):
    nums_2=[]
    new_num = 0
    for i in nums:
        new_num=i*random.randint(2,10)
        new_num+=random.randint(1,100)
        new_num+=i
        nums_2.append(new_num)
    print(nums_2)

change_number([1,2,3,7,8,9,12,20,40])


sum()
max()


