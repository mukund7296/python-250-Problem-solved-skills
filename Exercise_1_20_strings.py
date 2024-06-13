'''
Exercise 1 - Strings
Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.

How to solve a coding exercise:

Write your solution in the field below and then click on the Check Solution button.

If the solution you provide is incorrect, then try to understand the error message that appears on the right side of the screen, re-write your solution and press the Check Solution button again.

Finally, if you give up on this exercise and decide to move on, then click the Continue button.
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-1])

'''
Exercise 2 - Strings
Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[7])

'''
Exercise 3 - Strings
Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-10])

'''
Exercise 4 - Strings
Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.index('B'))

'''
Exercise 5 - Strings
Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string.
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.count('o'))

'''
Exercise 6 - Strings
Given the code below, insert the correct method on line 3 in order to convert all letters in the string to uppercase.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.upper())

'''
Exercise 7 - Strings
Given the code below, insert the correct method on line 3 in order to get the index at which the substring Bitcoin starts.
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.index('Bitcoin'))

'''
Exercise 8 - Strings
Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.startswith('X'))

'''
Exercise 9 - Strings
Given the code below, insert the correct method on line 3 in order to convert all uppercase letters to lowercase and all lowercase letters to uppercase.
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.swapcase())

'''
Exercise 10 - Strings
Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) from the string.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.replace(' ',''))

'''
Exercise 11 - Strings
Given the code below, insert the correct method on line 3 in order to replace all the occurrences of letter i with the substring btc.
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.replace('i','btc'))

'''
Exercise 12 - Strings
Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.split(','))

'''
Exercise 13 - Strings
Given the code below, insert the correct method on line 3 in order to join the characters of the string using the & symbol as a delimiter.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print("&".join(my_string))

'''
Exercise 14 - Strings
Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:

my_other_string = "Poor guy!"
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"

print(my_string+my_other_string)

'''
Exercise 15 - Strings
Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.

'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.capitalize())
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.title())

'''
Exercise 16 - Strings
Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
'''

my_string = "In %s, someone paid %s %s for two pizzas."

print(my_string%(2010, '10k', 'Bitcoin'))

'''
Exercise 17 - Strings
Given the code below, use string formatting with the format() method on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
'''
my_string = "In {}, someone paid {} {} for two pizzas."

print(my_string.format(2010, '10k', 'Bitcoin'))

'''
Exercise 18 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[3:7])

'''
Exercise 19 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!

'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-23:-16])

'''
Exercise 20 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:12])
