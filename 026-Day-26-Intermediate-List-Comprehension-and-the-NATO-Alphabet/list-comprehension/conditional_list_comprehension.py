names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# only want the names with 4 chars or lower
short_names = [name for name in names if len(name) <= 4]  # ['Alex', 'Beth', 'Dave']
print(short_names)


# if len is higher then 4 return them as upper case in list
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)
