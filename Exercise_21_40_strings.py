'''
Exercise 21 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-9:])

'''
Exercise 22 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::-1])

'''
Exercise 23 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return every 7th character of the string, starting with the first character.

The final result should be I,n top
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[0::7])

'''
Exercise 24 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!
'''
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[10:])

'''
Exercise 25 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:-4])

'''
Exercise 26 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to convert num1 from integer to float.
'''
num1 = 25

num2 = float(num1)

print(type(num2))

'''
Exercise 27 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to convert num1 from float to integer.

'''
num1 = 13.67

num2 = int(num1)

print(type(num2))


'''
Exercise 28 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.
'''
num1 = 25
num2 = 8

num3 = num1% num2

print(num3 == 1) #result is True

'''
Exercise 29 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.
'''
num1 = 10
num2 = 3

num3 = num1 **num2

print(num3 == 250 * 4) #result is True

'''
Exercise 30 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.
'''
num1 = 5
num2 = 2

num3 = num1 // num2

print(num3 == 5 % 3) #result is True

'''
Exercise 31 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to obtain the distance between num1 and 0.
'''
num1 = -11

num2 = abs(num1)

print(num2 == 11) #should result in True

'''
Exercise 32 - Numbers & Booleans
Given the code below, use the correct function on line 4 in order to raise num1 to the power of num2.
'''
num1 = 10
num2 = 5

num3 = num1 ** num2

print(num3 == 100000)

'''
Exercise 33 - Numbers & Booleans
Given the code below, use the correct logical operator in between the two expressions on line 1 in order for the final result to be False.
'''
result = ((25 % 7 + 10 / 2) % 3 == 0) and ((abs(-19) / 2 - 2) > 9)

print(result)  # should return False

'''
Exercise 34 - Numbers & Booleans
Given the code below, use the correct logical operator in between the two expressions on line 1 in order for the final result to be True.
'''
result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1) or (66 % 20 + 2 > 2 ** 3)

print(result)  # should return True


'''
Exercise 35 - Numbers & Booleans
Given the code below, use the correct function on line 1 (for which the argument sits inside the parentheses) in order for the final result to be False.

'''
result = bool(150 % (10 ** 2 / 2))

print(result)  # should return False

'''
Exercise 36 - Lists
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_list.
'''
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

char = len(my_list)

print(char)

'''
Exercise 37 - Lists
Given the code below, use the correct code on line 3 in order to remove the element of my_list located at index 5.
'''

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.remove('Java')

print(my_list)

'''
Exercise 38 - Lists
Given the code below, use the correct method on line 3 in order to add the element 'C++' at the end of my_list.

'''
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.append('C++')

print(my_list)

'''
Exercise 39 - Lists
Given the code below, use the correct method on line 3 in order to remove the element 30 from my_list.
'''
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.remove(30)

print(my_list)

'''
Exercise 40 - Lists
Given the code below, use the correct method on line 3 in order to return the index of the element 10.5 in my_list.
'''

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

index = my_list.index(10.5)

print(index)