import string

import random


password = ''
i= 1
while i <13:
    random_letter = random.choice(string.ascii_lowercase)

    password += random_letter

    i += 1

print(password)
    