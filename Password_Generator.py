import random

# Generate 2 random Lowercase characters
random1 = chr(random.randint(97, 122))
random2 = chr(random.randint(97, 122))

# Generate 2 random Uppercase characters
random3 = chr(random.randint(65, 90))
random4 = chr(random.randint(65, 90))

# Generate 2 random Digits
random5 = chr(random.randint(48, 57))
random6 = chr(random.randint(48, 57))

# Generate 2 random Symbols
random7 = chr(random.randint(33, 47))
random8 = chr(random.randint(33, 47))

# Concatenate the characters
password = random1 + random2 + random3 + random4 + random5 + random6 + random7 + random8

# Convert the password to a list of characters and shuffle it
password_list = list(password)
random.shuffle(password_list)

# Convert the shuffled list back to a string
shuffled_password = ''.join(password_list)

# Print the shuffled password
print(shuffled_password)