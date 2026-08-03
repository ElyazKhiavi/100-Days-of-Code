from random import random
import my_module
import random

print(random.random())
print(my_module.message)

for i in range(10):
    rand = round(random.random()*100)
    if rand <= 33:
        print('Rock', rand) 
    elif 33<rand<=66:
        print('Scissors', rand)
    else:
        print('Paper', rand)

for i in range(10):
    rand = round(random.uniform(1,99))
    if rand <= 33:
        print('Rock', rand) 
    elif 33<rand<=66:
        print('Scissors', rand)
    else:
        print('Paper', rand)


for i in range(10):
    rand = random.randint(1,3)
    if rand == 1:
        print('Rock', rand)
    elif rand == 2:
        print('Scissors', rand)
    else:
        print('Paper', rand)    



### Heads or Tails
num = random.randint(0,1)
if num == 1:
    print('Heads')
else:
    print('Tails')



# .choice
ls = [1,2,3,4]
random.choice(ls)

    
