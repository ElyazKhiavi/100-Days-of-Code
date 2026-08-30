# handling-exceptions
# try_except_else_finally


try:
    my_dict = {"key": "value"}
    my_dict["no_key"]
except KeyError:
    print("key does not exist")
else:
    print("All good")
finally:
    print("runs anyways!")
