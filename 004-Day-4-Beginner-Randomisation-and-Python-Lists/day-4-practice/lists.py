# Python Lists

# accessing items in a list
my_list = ["Item1", "Item2", "Item3"]
# print(my_list[9]) # IndexError!

print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])

# modify items in a list
my_list[2] = "Mirror"
print(my_list)

# can use input?!
the_list = [input("Enter item 1: "), input("Enter item 2: ")]
print(the_list)

# lists can have duplicates inside

my_new_list = [1, 1, 1, 2, 3, 4, 5, 5, 5]
print(my_new_list)  # [1, 1, 1, 2, 3, 4, 5, 5, 5]

# You can nest lists inside each other

nested_list = [
    ["apple", "orange", "cherry", "mango", "pineapple"],
    ["phone", "laptop", "tablet", "computer"],
    [["airplane", "helicopter", "jet"], ["car", "truck"]],
]
print(nested_list)

# can put variables inside a list
name = "Sam"
age = 30
married = True
height = 1.8


person_info = [name, age, height, married]
print(person_info)

for i in person_info:
    print(i, type(i))

# can add remove and modify the items in a list

person_info.append("He is Sad!")
person_info.insert(0, "here")
print(person_info)


ls = [0,1,2,"Mr.Black",3,4]
# ls.pop(2) # last item or the index inside
# ls.remove("Mr.Black") # give item
# print(ls)

if "Mr.Black" in ls:
    print("We found Him!")
