# with open("./my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", "a") as f:
    f.write("\nthis is cool")


with open("my_new_file.txt", mode="w") as f:
    f.write("New_file")
