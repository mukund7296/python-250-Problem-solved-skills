'''
Exercise 101 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a string.
'''
value = 10

conv = str(value)

print(type(conv))
'''
Exercise 102 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to an integer.
'''
value = "10"

conv = int(value)

print(type(conv))

'''
Exercise 103 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a floating-point number.
'''
value = "10"

conv = float(value)

print(type(conv))

'''
Exercise 104 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a list.
'''
value = "Hello!"

conv = list(value)

print(type(conv))

'''
Exercise 105 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a tuple.
'''
value = "Hello!"

conv = tuple(value)

print(type(conv))
'''
Exercise 106 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a frozen set.

'''
value = "Hello!"

conv = frozenset(value)

print(type(conv))


'''
Exercise 107 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a binary representation.
'''

value = 10

conv = bin(value)

print(type(conv))

'''
Exercise 108 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a hexadecimal representation.
'''

value = 10

conv = hex(value)

print(conv)

'''
Exercise 109 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value from binary to decimal notation.

'''
value = '0b1010'

conv = int(value, 2)

print(conv)
'''
 
Exercise 110 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value from hexadecimal to decimal notation.
'''
value = '0xa'

conv = int(value,16)

print(conv)

'''
Exercise 111 - Conditionals
Considering the code below, write code that prints out True! if x has 50 characters or more.
'''
x = "The days of Python 2 are almost over. Python 3 is the king now."

if len(x) >= 50:
    print("True!")

'''
Exercise 112 - Conditionals
Considering the code below, write code that prints out True! if x is a string and the first character in the string is T.
'''

x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[0]=='T':
    print('True!')

'''
Exercise 113 - Conditionals
Considering the code below, write code that prints out True! if at least one of the following conditions occurs:

the string contains the character z

the string contains the character y at least twice
'''
x = "The days of Python 2 are almost over. Python 3 is the king now."

if 'z' in x or x.count('y') >= 2:
    print("True!")

'''
Exercise 114 - Conditionals
Considering the code below, write code that prints out True! if the index of the first occurrence of letter f is less than 10 and prints out False! if the same condition is not satisfied.
'''
x = "The days of Python 2 are almost over. Python 3 is the king now."

index_of_f = x.find('f')

if index_of_f != -1 and index_of_f < 10:
    print("True!")
else:
    print("False!")

'''
Exercise 115 - Conditionals
Considering the code below, write code that prints out True! if the last 3 characters of the string are all digits and prints out False! otherwise.

Hint! Use the appropriate method to check if the requested string slice contains digits only.
'''
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[-3:].isdigit():
    print("True!")
else:
    print("False!")

'''
Exercise 116 - Conditionals
Considering the code below, write code that prints out True! if x has at least 8 elements and the element positioned at index 6 is a floating-point number and prints out False! otherwise.
'''

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if len(x) >= 8 and isinstance(x[6], float):
    print("True!")
else:
    print("False!")

'''
Exercise 117 - Conditionals
Considering the code below, write code that prints out True! if the second string of the first list in x ends with the letter h and the first string of the second list in x also ends with the letter h, and prints out False! otherwise.
'''

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if x[3][1].endswith('h') and x[7][0].endswith('h'):
    print("True!")
else:
    print("False!")

'''
Exercise 118 - Conditionals
Considering the code below, write code that prints out True! if one of the following two conditions are satisfied and prints out False! otherwise.

the third string of the first list in x ends with the letter h

the second string of the second list in x also ends with the letter h
'''
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][2].endswith('h') or x[7][1].endswith('h'):
    print("True!")
else:
    print("False!")

'''
Exercise 119 - Conditionals
Considering the code below, write code that prints out True! if the largest value among the first 3 elements of the list is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False!

Hint! Use the appropriate slices to make the comparison.
'''

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

# Get the largest value among the first 3 elements
max_first_three = max(x[:3])

# Get the smallest value among the next 3 elements
min_next_three = min(x[3:6])

# Compare the values and print the result
if max_first_three <= min_next_three:
    print("True!")
else:
    print("False!")

'''
Exercise 120 - Conditionals
Considering the code below, write code that prints out True! if 115 appears at least once inside the list or if it is the first element in the list. Otherwise, print out False!

Hint! Use the appropriate method to check if 115 is the first element in the list.


'''

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

# Check if 115 appears at least once in the list or is the first element
if 115 in x or (len(x) > 0 and x[0] == 115):
    print("True!")
else:
    print("False!")

'''
Exercise 121 - Conditionals
Considering the code below, write code that prints out True! if the value associated with key number 5 is Perl or the number of key-value pairs in the dictionary divided by 5 returns a remainder less than 2. Otherwise, print out False!
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x.get(5) == "Perl" or len(x) % 5 < 2:
    print("True!")
else:
    print("False!")

'''
Exercise 122 - Conditionals
Considering the code below, write code that prints out True! if 3 is a key in the dictionary and the smallest value (alphabetically) in the dictionary is C#. Otherwise, print out False!
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if 3 in x.keys() and min(x.values()) == "C#":
    print("True!")
else:
    print("False!")

'''
Exercise 123 - Conditionals
Considering the code below, write code that prints out True! if the last character of the largest (alphabetically) value in the dictionary is n. Otherwise, print out False!
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

# Find the largest value alphabetically
largest_value = max(x.values())

# Check if the last character of the largest value is 'n'
if largest_value[-1] == 'n':
    print("True!")
else:
    print("False!")

'''
Exercise 124 - Conditionals
Considering the code below, write code that prints out True! if the largest key in the dictionary divided by the second largest key in the dictionary returns a remainder equal to the smallest key in the dictionary. Otherwise, print out False!
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
keys_sorted = sorted(x.keys())
largest_key = keys_sorted[-1]
second_largest_key = keys_sorted[-2]
smallest_key = keys_sorted[0]

# Calculate the remainder when dividing the largest key by the second largest key
remainder = largest_key % second_largest_key

# Check if the remainder is equal to the smallest key
if remainder == smallest_key:
    print("True!")
else:
    print("False!")
'''
Exercise 125 - Conditionals
Considering the code below, write code that prints out True! if the sum of all the keys in the dictionary is less than the number of characters of the string obtained by concatenating the values associated with the first 5 keys in the dictionary. Otherwise, print out False!
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

sum_of_keys = sum(x.keys())

# Concatenate the values associated with the first 5 keys into a single string
concatenated_string = "".join([x[key] for key in range(1, 6)])

# Find the length of the concatenated string
length_of_concatenated_string = len(concatenated_string)

# Compare the sum of keys with the length of the concatenated string
if sum_of_keys < length_of_concatenated_string:
    print("True!")
else:
    print("False!")
