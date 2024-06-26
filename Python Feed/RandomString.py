import random
import string

# Function to generate a random string of fixed length
def random_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a list of 10 random 5-character strings
random_strings = [random_string(5) for _ in range(10)]

# Print the list of random strings
print(random_strings)
