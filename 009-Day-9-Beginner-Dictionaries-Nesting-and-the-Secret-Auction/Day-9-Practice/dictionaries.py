# Dictionaries in Python

test_dict = {
    "key1": "value1",
    "key2": "value2",
}
character = {
    "Name": "Monkey D. Luffy",
    "NickName": "Jesus of Nazareth",
    "Age": 19,
    "Race": "Human",
    "Eye Color": "Black",
    "Hair Color": "Black",
    "Personality": [
        "Unshakably Confident",
        "Fiercely Loyal",
        "Obsessed with Meat",
        "Completely Fearless",
    ],
}

my_dict = {"name":"john", "age":5, "index":2003}

print(my_dict["name"]) # john
# print(my_dict[1]) # error

test_dict["key1"] # value1
test_dict["key3"] ="value3"  # Assign
test_dict["key2"] = "new value"  # ReAssign

print(test_dict)
print(character["Name"])

for key, value in character.items():
    print(f"{key}: {value}")

# for key in character:
#     print(key,":",character[key])
