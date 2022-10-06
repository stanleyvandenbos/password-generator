from http.client import TEMPORARY_REDIRECT
import numbers
import random, string

# Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Settings
length = int(input('\nEnter the length of your password: '))
print("\nSome websites don't allow symbols.")
use_symbols = input('\nDo you want to use symbols? (yes/no): ')

if use_symbols() == 'yes':
    data = lower + upper + num + symbols

elif use_symbols() == 'no':
    data = lower + upper + num

else:
    print('Type yes or no')

# Use random
temp = random.sample(all,length)

# Generate password
password = "".join(temp)

print(password)
