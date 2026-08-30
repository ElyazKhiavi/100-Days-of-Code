raise ValueError("This is an error I raised!")  # !!!!


x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
