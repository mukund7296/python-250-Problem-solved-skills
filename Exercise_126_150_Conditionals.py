'''
Exercise 126 - Conditionals
Considering the code below, write code that prints out True! if the 3rd element of the first range is less than 2, prints out False! if the 5th element of the first range is 5, and prints out None! otherwise.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if len(x[0]) > 2 and x[0][2] < 2:
    print("True!")
elif len(x[0]) > 4 and x[0][4] == 5:
    print("False!")
else:
    print("None!")

'''
Exercise 127 - Conditionals
Considering the code below, write code that prints out True! if the 3rd element of the 3rd range is less than 6, prints out False! if the 1st element of the second range is 5, and prints out None! otherwise.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Check conditions
if len(x) > 2 and len(x[2]) > 2 and x[2][2] < 6:
    print("True!")
elif len(x) > 1 and len(x[1]) > 0 and x[1][0] == 5:
    print("False!")
else:
    print("None!")

'''
Exercise 128 - Conditionals
Considering the code below, write code that prints out True! if the last element of the first range is greater than 3, prints out False! if the last element of the second range is less than 9, and prints out None! otherwise.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Check conditions
if x[0][-1] > 3:
    print("True!")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None!")
'''
Exercise 129 - Conditionals
Considering the code below, write code that prints out True! if the length of the first range is greater than or equal to 5, prints out False! if the length of the second range is 4, and prints out None! otherwise.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Check conditions
if len(x[0]) >= 5:
    print("True!")
elif len(x[1]) == 4:
    print("False!")
else:
    print("None!")
'''
Exercise 130 - Conditionals
Considering the code below, write code that prints out True! if the sum of all the elements of the first range is greater than the sum of all the elements of the third range, prints out False! if the largest element of the second range is greater than the largest element of the third range, and prints out None! otherwise.
'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Calculate sums and maximums
sum_first = sum(x[0])
sum_third = sum(x[2])
max_second = max(x[1])
max_third = max(x[2])

# Check conditions
if sum_first > sum_third:
    print("True!")
elif max_second > max_third:
    print("False!")
else:
    print("None!")
'''
Exercise 131 - Conditionals
Considering the code below, write code that prints out True! if the largest element of the first range minus the second element of the 3rd range is equal to the first element of the first range, prints out False! if the length of the first range minus the length of the 2nd range is equal to the first element of the 3rd range, prints out Maybe! if the sum of all the elements of the 3rd range divided by 2 returns a remainder of 0, and prints out None! otherwise.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Extract elements and lengths
largest_first = max(x[0])
second_third = x[2][1]
first_first = x[0][0]
len_first = len(x[0])
len_second = len(x[1])
first_third = x[2][0]
sum_third = sum(x[2])

# Check conditions
if largest_first - second_third == first_first:
    print("True!")
elif len_first - len_second == first_third:
    print("False!")
elif sum_third % 2 == 0:
    print("Maybe!")
else:
    print("None!")
'''

Exercise 132 - Conditionals
Considering the code below, write code that prints out True! if the sum of the last 3 elements of the first range plus the sum of the last 3 elements of the 3rd range is equal to the sum of the last 3 elements of the 2nd range, and prints out False! if the length of the first range times 2 is less than the sum of all the elements of the 3rd range.
'''
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

# Calculate sums and lengths
sum_last_3_first = sum(x[0][-3:])
sum_last_3_third = sum(x[2][-3:])
sum_last_3_second = sum(x[1][-3:])
len_first_times_2 = len(x[0]) * 2
sum_third_all = sum(x[2])

# Check conditions
if sum_last_3_first + sum_last_3_third == sum_last_3_second:
    print("True!")
elif len_first_times_2 < sum_third_all:
    print("False!")
else:
    print("None!")


'''
Exercise 133 - Conditionals
Considering the code below, write code that prints out True! if the 2nd character of the value at key 1 is also present in the value at key 4, and prints out False! otherwise.
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[1][1] in x[4]:
    print("True!")
else:
    print("False!")
'''
Exercise 134 - Conditionals
Considering the code below, write code that prints out True! if the second to last character of the value at key 3 is the first character of the value at key 5, and prints out False! otherwise.
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

second_last_char_key_3 = x[3][-2]

# Extract first character of value at key 5
first_char_key_5 = x[5][0]

# Check if second-last character of key 3 is equal to first character of key 5
if second_last_char_key_3 == first_char_key_5:
    print("True!")
else:
    print("False!")

'''
Exercise 135 - Conditionals
Considering the code below, write code that prints out True! if the number of characters of the smallest value in the dictionary is equal to the number of occurrences of letter a in the value at key 3, and prints out False! otherwise.
'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

smallest_value = min(x.values(), key=len)

# Calculate the number of characters in the smallest value
num_chars_smallest_value = len(smallest_value)

# Count occurrences of 'a' in the value at key 3
num_a_in_key_3 = x[3].count('a')

# Check if the number of characters in the smallest value equals the number of 'a's in key 3
if num_chars_smallest_value == num_a_in_key_3:
    print("True!")
else:
    print("False!")

'''
Exercise 136 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list.
'''
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in x:
    print(i)

'''
Exercise 137 - Loops
Write a for loop that iterates over the x list and prints out the remainders of each element of the list divided by 3.
'''

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for element in x:
    # Calculate the remainder when element is divided by 3
    remainder = element % 3
    # Print the remainder
    print(remainder)


'''
Exercise 138 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list in reversed order and multiplied by 10.
'''
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for element in reversed(x):
    print(element * 10)

'''
Exercise 139 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list divided by 2 and the string Great job! after the list is exhausted.

'''
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in x:
    print(i/2)
print("Great job!")

'''
Exercise 140 - Loops
Write a for loop that iterates over the x list and prints out the index of each element.
'''

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for index, element in enumerate(x):
    # Print the index of each element
    print(index)

'''
Exercise 141 - Loops
Write a while loop that prints out the value of x squared while x is less than or equal to 5. Be careful not to end up with an infinite loop!

'''
x = 0

while x<=5:
    print(x**2)
    x+=1
'''
Exercise 142 - Loops
Write a while loop that prints out the value of x times 10 while x is less than or equal to 4 and then prints out Done! when x becomes larger than 4. Be careful not to end up with an infinite loop!
'''
x = 0

while x <= 4:
    print(x * 10)
    x += 1

print("Done!")
'''
Exercise 143 - Loops
Write a while loop that prints out the value of x plus 10 while x is less than or equal to 15 and the remainder of x divided by 5 is 0. Be careful not to end up with an infinite loop!
'''
x = 10

while x <= 15 and x % 5 == 0:
    print(x + 10)
    x = x + 1


'''
Exercise 144 - Loops
Write a while loop that prints out the absolute value of x while x is negative. Be careful not to end up with an infinite loop!
'''
x = -7

while x < 0:
    print(abs(x))
    x += 1

'''
Exercise 145 - Loops
Write a while loop that prints out the value of x times y while x is greater than or equal to 5 and less than 10, and prints out the result of x divided by y when x becomes 10. Be careful not to end up with an infinite loop!
'''
x = 5
y = 2

while x < 10:
    if x >= 5 and x < 10:
        print(x * y)
    x += 1

if x == 10:
    print(x / y)

'''
Exercise 146 - Loops
Write code that will iterate over the x list and multiply by 10 only the elements that are greater than 20 and print them out to the screen.

Hint: use nesting!
'''
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for num in x:
    if num > 20:
        multiplied = num * 10
        print(multiplied)
'''
Exercise 147 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y, also printing the results to the screen.

Hint: use nesting!
'''
x = [2, 4, 6]
y = [5, 10]

for num_x in x:
    for num_y in y:
        result = num_x * num_y
        print(result)
'''
Exercise 148 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than 12, also printing the results to the screen.

Hint: use nesting!
'''
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for num_x in x:
    for num_y in y:
        if num_y < 12:
            result = num_x * num_y
            print(result)


'''
Exercise 149 - Loops
Write code that will iterate over the x and y lists and multiply each element of x that is greater than 5 with each element of y that is less than 12, also printing the results to the screen.

Hint: use nesting!
'''

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for num_x in x:
    if num_x > 5:
        for num_y in y:
            if num_y < 12:
                result = num_x * num_y
                print(result)

'''
Exercise 150 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than or equal to 10, also printing the results to the screen. For y's elements that are greater than 10, multiply each element of x with y squared.

Hint: use nesting!
'''

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for num_x in x:
    for num_y in y:
        if num_y <= 10:
            result = num_x * num_y
        else:
            result = num_x * (num_y ** 2)
        print(result)
