'''
Exercise 61 - Sets
Given the code below, use the correct function on line 3 in order to convert my_list to a set.
'''
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = set(my_list)

print(type(my_set))

'''
Exercise 62 - Sets
Given the code below, use the correct function on line 3 in order to convert my_list to a frozen set.

'''
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = frozenset(my_list)

print(type(my_set))

'''
Exercise 63 - Sets
Given the code below, use the correct code on line 3 in order to verify if element 10 is in my_set.
'''

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

check = 10 in my_set

print(check)

'''
Exercise 64 - Sets
Given the code below, use the correct method on line 3 in order to add the element 19 to my_set.
'''

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.add(19)

print(my_set)

'''
Exercise 65 - Sets
Given the code below, use the correct method on line 3 in order to delete the element 9 from my_set.
'''
my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.remove(9)

print(my_set)

'''
Exercise 66 - Sets
Given the code below, use the correct method on line 4 in order to find out the common elements of my_set1 and my_set2.
'''
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

common = my_set1.intersection(my_set2)

print(sorted(list(common)))

'''
Exercise 67 - Sets
Given the code below, use the correct method on line 4 in order to join the elements of my_set1 and my_set2.
'''
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = my_set1.union(my_set2)

print(sorted(list(join)))

'''
Exercise 68 - Sets
Given the code below, use the correct method on line 4 in order to find out the elements of my_set2 that are not members of my_set1.
'''

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = my_set2.difference(my_set1)

print(sorted(list(diff)))

'''
Exercise 69 - Tuples
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_tup.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

number = len(my_tup)

print(number)

'''
Exercise 70 - Tuples
Given the code below, use the correct method on line 3 in order to find out the index of Slovakia in my_tup.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

index = my_tup.index('Slovakia')

print(index)

'''
Exercise 71 - Tuples
Given the code below, write code in order to perform tuple assignment on line 3 and obtain the results below.

'''

my_tup = ("Romania", "Poland", "Estonia")

ro, po, es = my_tup

print(ro + ", " + po + ", " + es)  # returns 'Romania, Poland, Estonia'

'''
Exercise 72 - Tuples
Given the code below, use the correct method on line 3 in order to find out the last element of my_tup in alphabetical order.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

last = max(my_tup)

print(last) #should return Slovenia

'''
Exercise 73 - Tuples
Given the code below, use the correct method on line 3 in order to find out the number of occurrences of Estonia in my_tup.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.count('Estonia')

print(number)

'''
Exercise 74 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first two of them, using a negative index.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[2:]

print(my_slice)

'''
Exercise 75 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last three of them, using a negative index.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:-3]

print(my_slice)

'''
Exercise 76 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first three of them, using a positive index.
'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[3:]

print(my_slice)

'''
Exercise 77 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last two of them, using a positive index.
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:-2]

print(my_slice)

'''

Exercise 78 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 0 to 9 inclusively. Use a single argument inside the parentheses of range()!
'''
my_range = range(10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


'''
Exercise 79 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 0 to 9 inclusively. Use two arguments inside the parentheses of range()!

'''

my_range = range(10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
Exercise 80 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 117 to 129 exclusively.


'''


my_range = range(117,129)

print(list(my_range)) #[117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]