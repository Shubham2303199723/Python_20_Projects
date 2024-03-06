import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
sysmbols = "!@#$%^&*()_-+=?><["

all_chars = lower + upper + numbers + sysmbols
lenght = int(input("Enter Lenght of Password "))

password = ''.join(random.sample(all_chars, lenght))
print("Generated Password ", password)