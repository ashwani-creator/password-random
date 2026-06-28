import random
import string

length = int(input("Enter password length: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lower + upper + digits + symbols

temp_password = random.sample(all_characters, length)
password = "".join(temp_password)
print("Generated Password:", password)