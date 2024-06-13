'''
Exercise 226 - Regular Expressions
Write code on line 5 in order to replace all the years in the string with XXXX using the sub() method.

'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.sub(r"\s\d{4}", " XXXX", s)

print(result)

'''
Exercise 227 - Regular Expressions
Write code on line 5 in order to replace each floating-point number in the string (10,259.02 and 0.10) with a dot (.) using the sub() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.sub(r"\d{1,},*\d*\.\d{1,}", ".", s)

print(result)



'''
Exercise 228 - Regular Expressions
Write code on line 5 in order to replace all occurrences of BTC in the string with Bitcoin using the sub() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.sub(r"[A-Z]{3}", "Bitcoin", s)

print(result)
'''

Exercise 229 - Regular Expressions
Write code on line 5 in order to replace all the digits less than or equal to 5 in the string with 8 using the sub() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.sub(r"[0-5]", "8", s)

print(result)

'''
Exercise 230 - Regular Expressions
Write code on line 5 in order to replace all the words starting with an uppercase letter or digits greater than or equal to 6 in the string with W using the sub() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.sub(r"[A-Z]\w{1,}|[6-9]", "W", s)

print(result)
'''
Exercise 231 - Classes
Write a class called ClassOne starting on line 1 containing:

The __init__ method with two parameters p1 and p2. Define the corresponding attributes inside the __init__ method.

A method called square that takes one parameter p3 and prints out the value of p3 squared.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)
print(type(p))


'''
Exercise 232 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to access the p1 attribute for the current instance of the class and print its value to the screen.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

print(p.p1)


'''

Exercise 233 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to call the square() method for the current instance of the class using 10 as an argument and print the result to the screen.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

p.square(10)

'''
Exercise 234 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to set the value of the p2 attribute to 5 for the current instance of the class, without using a function.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

p.p2 = 5

print(p.p2)


'''
Exercise 235 - Classes
Considering the ClassOne class and the p object, write code on lines 11 and 12 in order to set the value of the p2 attribute to 50 for the current instance of the class using a function, and then get the new value of p2, again using a function, and print it out to the screen as well.

'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

setattr(p, 'p2', 50)
print(getattr(p, 'p2'))

'''
Exercise 236 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to check if p2 is an attribute of p, using a function, also printing the result to the screen.
'''

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

print(hasattr(p, 'p2'))

'''
Exercise 237 - Classes
Considering the ClassOne class and the p object, write code on line 11 to check if p is indeed an instance of the ClassOne class, using a function, also printing the result to the screen
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


p = ClassOne(1, 2)

print(isinstance(p, ClassOne))

'''
Exercise 238 - Classes
Considering the ClassOne class, write code starting on line 9 to create a child class called ClassTwo that inherits from ClassOne and also has its own method called times10() that takes a single parameter x and prints out the result of multiplying x by 10.


'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


class ClassTwo(ClassOne):
    def times10(self, x):
        print(x * 10)


y = ClassTwo(10, 20)
print(y.p1)

'''
Exercise 239 - Classes
Considering the ClassOne and ClassTwo classes, where the latter is a child of the former, write code on line 15 in order to call the times10() method from the child class having x equal to 45, also printing the result to the screen.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10


obj = ClassTwo(15, 25)

print(obj.times10(45))
'''
Exercise 240 - Classes
Considering the ClassOne and ClassTwo classes, write code on line 13 to verify that ClassTwo is indeed a child of ClassOne, also printing the result to the screen.
'''


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def square(self, p3):
        print(p3 ** 2)


class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10


print(issubclass(ClassTwo, ClassOne))


'''
Exercise 241 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(1, 5) and return a list of its elements.
'''
cph = [i for i in range(1, 5)]

print(cph)


'''
Exercise 242 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(1, 15, 5) and return a list of its elements squared.
'''

cph = [i ** 2 for i in range(1, 15, 5)]

print(cph)

'''
Exercise 243 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(5, 25, 3) and return a list of its elements squared only for the elements that are less than or equal to 16.
'''
cph = [i ** 2 for i in range(5, 25, 3) if i <= 16]

print(cph)


'''
Exercise 244 - Other Concepts
Write a dictionary comprehension on line 1 that will iterate over range(9) and return a dictionary of key-value pairs where the value is equal to the key times 3.
'''
cph = {x: x * 3 for x in range(9)}

print(cph)



'''

Exercise 245 - Other Concepts
Write a set comprehension on line 1 that will iterate over range(10, 19) and return a set of its elements divided by 2.5.


'''
cph = {x / 2.5 for x in range(10, 19)}

print(cph)


'''
Exercise 246 - Other Concepts
Write a lambda function on line 1 that takes two parameters x and y and multiplies x with y.
'''
lam = lambda x, y: x * y

print(lam(2, 5))

'''
Exercise 247 - Other Concepts
Write a lambda function on line 1 that takes a list list1 as a parameter, and multiplies each element of range(1, 5) with each element of list1 using a list comprehension.
'''

lam = lambda list1: [x * y for x in range(1, 5) for y in list1]

print(lam([1, 2]))

'''
Exercise 248 - Other Concepts
Use the correct function from the itertools module on line 6, in between the parentheses of list(), in order to concatenate list1 and list2.
'''
import itertools

list1 = [1, 2, 3]
list2 = [4, 5]

result = list(itertools.chain(list1, list2))

print(result)

'''
Exercise 249 - Other Concepts
Use the correct function from the itertools module with a for loop and a nested if/else block in order to return all the numbers starting at 20 and up to 31 with a step of 2. Be careful not to end up with an infinite loop!
'''

import itertools

for i in itertools.count(20, 2):
    if i < 31:
        print(i)
    else:
        break

'''
Exercise 250 - Other Concepts
Use the correct function from the itertools module on line 5, in between the parentheses of list(), in order to return the elements for which the lambda function given as an argument returns False.
'''
import itertools

lam = lambda x: x < 5

result = list(itertools.filterfalse(lam, range(10)))

print(result)