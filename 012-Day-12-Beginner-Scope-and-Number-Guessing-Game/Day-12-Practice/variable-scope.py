# variable-scope.py



my_num = 20 # <- global

def change_num():
    my_num = 15 # <- local
    print(my_num)


change_num()
print(my_num)



new_num = 39

def change_global():
    global new_num # <-- now has access to modify the global scope
    new_num+=15
    print(f"Inside function: {new_num}")

change_global()
print(f"Outside function: {new_num}")