# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Daniel'
age = 28

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# Comma
print('Hello, my name is', name, 'and I am', age)

# String Methods
s = 'hello world'

# Capitalize string
print('capitalize():', s.capitalize())

# Make all titlecase
print('title():', s.title())

# Make all uppercase
print('upper():', s.upper())

# Make all lower
print('lower():', s.lower())

# Swap case
print('swapcase():', s.swapcase())

# Get length
print('len():', len(s))

# Replace
print('replace():', s.replace('world', 'everyone'))

# Count
sub = 'h'
print('sub():', s.count(sub))

# Starts with
print('startswith():', s.startswith('hello'))

# Ends with
print('endswith():', s.endswith('d'))

# Split into a list
print('split():', s.split())

# Find position
print('find():', s.find('r'))

# Is all alphanumeric
print('isalnum():', s.isalnum())

# Is all alphabetic
print('isalpha():', s.isalpha())

# Is all numeric
print('isnumeric()', s.isnumeric())
