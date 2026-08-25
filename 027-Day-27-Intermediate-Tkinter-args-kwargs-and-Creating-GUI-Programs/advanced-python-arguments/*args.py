def add_nums(*args):
    return sum(args)


def avg_of_nums(*args):
    return f"{(sum(args)/len(args)):.2f}"


def max_num(*args):
    return max(args)


def min_num(*args):
    return min(args)


print(add_nums(9, 82, 83, 839, -39, 39, -394))
print(avg_of_nums(9, 82, 83, 839, -39, 39, -394))
print(max_num(9, 82, 83, 839, -39, 39, -394))
print(min_num(9, 82, 83, 839, -39, 39, -394))





