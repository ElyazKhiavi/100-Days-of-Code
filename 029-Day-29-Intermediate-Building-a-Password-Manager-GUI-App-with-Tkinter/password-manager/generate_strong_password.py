# generate_strong_password

import secrets
import string
import random

# alphabet = string.ascii_letters+string.digits+string.punctuation
alphabet = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

password1 = "".join(secrets.choice(alphabet) for i in range(32))
password2 = "".join(random.choice(alphabet) for i in range(32))

# print(alphabet)
print(password1)
print(password2)
