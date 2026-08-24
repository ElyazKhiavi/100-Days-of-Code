num = 1234
nums_list = [int(i) for i in str(num)]
nums_list.reverse()

print(nums_list)

n = 12343211
name_list = [n for n in str(n)]
rev_name_list = name_list[::-1]

print(name_list)
print(rev_name_list)
print(name_list == rev_name_list)

