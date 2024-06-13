'''
Exercise 176 - Functions
Implement a function called my_func() that takes a single parameter x and multiplies it with each element of range(5), also adding each multiplication result to a new (initially empty) list called my_new_list. Finally, the list should be printed out to the screen after the function is called.
'''
def my_func(x):
    my_new_list = []
    for i in range(5):
        my_new_list.append(x * i)
    return my_new_list

result = my_func(2)
print(result)

'''
Exercise 177 - Functions
Implement a function called my_func() that takes a single parameter x (a string) and turns each character of the string to uppercase, also returning the result when the function is called.
'''
def my_func(x):
    return x.upper()

result = my_func("Satoshi Nakamoto")
print(result)

'''
Exercise 178 - Functions
Implement a function called my_func() that takes a single parameter x (a list) and eliminates all duplicates from the list, also returning the result when the function is called.
'''
def my_func(x):
    return list(set(x))

result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)

'''
Exercise 179 - Functions
Implement a function called my_func() that takes a single parameter x (a tuple) and for each element of the tuple that is greater than 4 it raises that element to the power of 2, also adding it to a new (initially empty) list called my_new_list. Finally, the code returns the result when the function is called.
'''


def my_func(x):
    my_new_list = []
    for i in x:
        if i > 4:
            my_new_list.append(i ** 2)
    return my_new_list


result = my_func((2, 3, 5, 6, 4, 8, 9))
print(result)

'''
Exercise 180 - Functions
Implement a function called my_func() that takes a single parameter x (a dictionary) and multiplies the number of elements in the dictionary with the largest key in the dictionary, also returning the result when the function is called.
'''
def my_func(x):
    num_elements = len(x)  # Number of elements in the dictionary
    largest_key = max(x.keys())  # Largest key in the dictionary

    result = num_elements * largest_key

    return result

result = my_func({1: 3, 2: 3, 4: 5, 5: 9, 6: 8, 3: 7, 7: 0})
print(result)

'''
Exercise 181 - Functions
Implement a function called my_func() that takes a single positional parameter x and a default parameter y which is equal to 10 and multiplies the two, also returning the result when the function is called.
'''
def my_func(x, y=10):
    result = x * y
    return result


result = my_func(5)
print(result)

'''
Exercise 182 - Functions
Implement a function called my_func() that takes a single positional parameter x and two default parameters y and z which are equal to 100 and 200 respectively, and adds them together, also returning the result when the function is called.
'''
def my_func(x, y=100, z=200):
    result = x + y + z
    return result


result = my_func(50)
print(result)

'''
Exercise 183 - Functions
Implement a function called my_func() that takes two default parameters x (a list) and y (an integer), and returns the element in x positioned at index y, also printing the result to the screen when called.
'''


def my_func(x, y):
    return x[y]


result = my_func(list(range(2, 25, 2)), 4)
print(result)

'''
Exercise 184 - Functions
Implement a function called my_func() that takes a positional parameter x and a variable-length tuple of parameters and returns the result of multiplying x with the second element in the tuple, also returning the result when the function is called.

'''
def my_func(x, *args):

    if len(args) >= 2:
        result = x * args[1]
        return result
    else:
        return None

result = my_func(5, 10, 20, 30, 50)
print(result)

'''
Exercise 185 - Functions
Implement a function called my_func() that takes a positional parameter x and a variable-length dictionary of (keyword) parameters and returns the result of multiplying x with the largest value in the dictionary, also returning the result when the function is called.
'''


def my_func(x, **kwargs):
    if kwargs:
        largest_value = max(kwargs.values())
        result = x * largest_value
        return result
    else:
        return None


result = my_func(10, val1=10, val2=15, val3=20, val4=25, val5=30)
print(result)

'''
Exercise 186 - Functions
Add the correct line(s) of code inside the function in order to get 200 as a result of calling my_func() and have the result printed out to the screen.
'''

var = 10


def my_func(x):
    print(x * var)


my_func(20)


'''
Exercise 187 - Functions
Add the correct line(s) of code inside the function in order to get 100 as a result of calling my_func() and have the result printed out to the screen.
'''
var = 10

def my_func(x):
    var = 5
    print(x * var)


my_func(20)


'''
Exercise 188 - Functions
Make the necessary adjustment inside the function in order to get 120 as a result of calling my_func() and have the result printed out to the screen.

'''
def my_func(x):
    global var
    var = 12
    print(x * var)

my_func(10)

'''
Exercise 189 - Functions
Add the necessary line of code inside the function in order to get 80 as a result of calling my_func() and have the result printed out to the screen.
'''
var = 8


def my_func(x):
    global var
    print(x * var)
    var = 12


my_func(10)

'''
Exercise 190 - Functions
Write code that will import only the pi variable from the math module and then it will format it in order to have only 4 digits after the floating point. Of course, print out the result to the screen using the print() function.
'''


from math import pi

formatted_pi = f"{pi:.4f}"
print(formatted_pi)

'''
Exercise 191 - Files
Add the necessary code in between print's parentheses in order to read the content of test.txt as a string and have the result printed out to the screen.
'''
f = open("test.txt", "r")

content = f.read()
print(content)


'''

Exercise 192 - Files
Add the necessary code in between print's parentheses in order to read the content of test.txt as a list where each element of the list is a row in the file, and have the result printed out to the screen.
'''
f = open("test.txt", "r")
lines = f.readlines()
print(lines)

'''
Exercise 193 - Files
Add the necessary code on line 5 in order to bring back the cursor at the very beginning of test.txt before reading from the file once again.
'''
f = open("test.txt", "r")

f.read()

f.seek(0)

print(f.read())

'''
Exercise 194 - Files
Add the necessary code on line 5 (in between the parentheses of print()) in order to get the current position of the cursor inside test.txt and have the result printed out to the screen.
'''

f = open("test.txt", "r")

f.read(5)

print(f.tell())

'''
Exercise 195 - Files
Add the necessary code on line 5 (in between the parentheses of print()) in order to get the current mode in which test.txt is open (read, write etc.) and have the result printed out to the screen.
'''
f = open("test.txt", "r")

f.read(5)

mode = f.mode

print(mode)

f.close()
'''
Exercise 196 - Files
Add the necessary file access mode on line 1 in order to open test.txt for appending and reading at the same time.
'''
f = open("test.txt",'a+' )

print(f.mode)

'''
Exercise 197 - Files
Add the necessary code on lines 3 and 4 in order to write the string python to test.txt and have the result of reading the file printed out to the screen.
'''
f = open("test.txt", "w")
f.write("python")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()  # Always close the file after operations are complete


'''
Exercise 198 - Files
Add the necessary code on lines 3 and 4 in order to write a list of strings ['python', ' ', 'and', ' ', 'java'] to test.txt and have the result of reading the file printed out to the screen.
'''
# Open the file in write mode ("w")
f = open("test.txt", "w")

# Define the list of strings to write to the file
strings_list = ['python', ' ', 'and', ' ', 'java']

# Write each string from the list to the file
for string in strings_list:
    f.write(string)

# Close the file after writing
f.close()

# Open the file in read mode ("r")
f = open("test.txt", "r")

# Read and print the contents of the file
print(f.read())

# Close the file after reading
f.close()

'''
Exercise 199 - Files
Add the necessary code starting at line 1 in order to write the string python and also close test.txt properly using the with statement.
'''

with open("test.txt", "w") as f:
    f.write("python")



f = open("test.txt", "r")

print(f.read())

'''
Exercise 200 - Files
Add the necessary code on lines 4 and 5 in order to delete the entire content of test.txt.
'''

with open("test.txt", "w") as f:
    f.write("python")

with open("test.txt", "w") as f:
    pass  # This effectively clears the content by truncating the file

with open("test.txt", "r") as f:
    print(f.read())



