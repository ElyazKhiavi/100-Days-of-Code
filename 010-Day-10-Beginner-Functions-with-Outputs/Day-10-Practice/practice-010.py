stringNumber = input("Enter the Float Value.\n")


# def is_float(s):
#     if s.count(".") == 1 and s.replace(".", "").isdigit():
#         return float(s)
#     else:
#         return False


def is_float(s):
    # remove leading minus if present
    s_no_minus = s.lstrip('-')
    if not s_no_minus or s.count("-")>1:                    # string was just "-"
        return None
    if s_no_minus.count('.') > 1:         # more than one dot → invalid
        return None
    # remove the dot (if any)
    s_no_dot = s_no_minus.replace('.', '', 1)
    if not s_no_dot or not s_no_dot.isdigit():
        return None
    # now we can safely convert
    return float(s)


# If the Input String is Number Print the Number
if is_float(stringNumber) is not None:
    print("{} is Float".format(stringNumber))
else:
    print("Error: Not a Float Value.")
