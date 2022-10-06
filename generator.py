import random, string

# Choises
yes = ['yes', 'y']
no = ['no', 'n']

# Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Questions
while True:
    
    try:
        length = int(input('Enter the length of your password: '))
        break

    except ValueError:
        print('\nThis is not a number. Try again...')
        continue

print("\nSome websites don't allow symbols.")

while True:

    use_symbols = input('Do you want to use symbols? (yes/no): ')

    if use_symbols.lower() in yes:
        data = lower + upper + num + symbols
        break

    elif use_symbols.lower() in no:
        data = lower + upper + num
        break

    else:
        print('\nType yes or no...')
        continue

# Use random
temp = random.sample(data,length)

# Generate password
password = "".join(temp)

print('\nPassword:\n' + password)
