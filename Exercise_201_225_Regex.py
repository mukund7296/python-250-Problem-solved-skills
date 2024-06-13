'''
Exercise 201 - Regular Expressions
Write code on line 5 in order to match the word Bitcoin at the beginning of the string using the match() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.match('Bitcoin',s)

print(result.group())

'''
Exercise 202 - Regular Expressions
Write code on line 5 in order to match the word Bitcoin at the beginning of the string using the match() method and ignoring the case. This way, no matter if you have bitcoin or Bitcoin, the match is done either way.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."


pattern = r"^bitcoin"  # Adjusted pattern to match "bitcoin" or "Bitcoin" at the beginning, ignoring case
result = re.match(pattern, s, re.IGNORECASE)  # Using re.IGNORECASE to ignore case sensitivity

if result:
    print(result.group())
else:
    print("No match found.")

'''
Exercise 203 - Regular Expressions
Write code on line 5 in order to match the words Bitcoin was at the beginning of the string using the match() method. Use the dot (.) belonging to regex syntax in your solution.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.match(r"B.{6} .{3}", s)

print(result.group())
'''
Exercise 204 - Regular Expressions
Write code on line 5 in order to match the year 2009 in the string using the search() method. Use the \d in your solution.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r"(\d{4})\s", s)

print(result.group(1))

'''
Exercise 205 - Regular Expressions
Write code on line 5 in order to match the year 2017 in the string using the search() method. Use the \d in your solution.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r"(\d{4}),", s)

print(result.group(1))

'''
Exercise 206 - Regular Expressions
Write code on line 5 in order to match the date Jan 3rd 2009 in the string using the search() method. Use the \d in your solution.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r"(.{3}\s\d\w\w\s\d{4})\s", s)

print(result.group(1))

'''

Exercise 207 - Regular Expressions
Write code on line 5 in order to match BTC in the string using the search() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r'BTC', s)

if result:
    print(result.group())
else:
    print("No match found.")

'''
Exercise 208 - Regular Expressions
Write code on line 5 in order to match 1 BTC in the string using the search() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r"([0-9]\s[A-Z]{3})", s)

print(result.group(1))
'''
Exercise 209 - Regular Expressions
Write code on line 5 in order to match $20000 in the string using the search() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r'\$20000', s)

if result:
    print(result.group())
else:
    print("No match found.")

'''
Exercise 210 - Regular Expressions
Write code on line 5 in order to match $300B in the string using the search() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.search(r'\$300B', s)

print(result.group() if result else "No match found.")


'''
Exercise 211 - Regular Expressions
Write code on line 5 in order to match market cap of in the string using the search() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r'market cap of', s)

print(result.group() if result else "No match found.")

'''
Exercise 212 - Regular Expressions
Write code on line 5 in order to match 184,073,529,068 in the string using the search() method.
'''
import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r"\$(\d{3},[0-9]{3},\d{3},[0-9]{3}),", s)

print(result.group(1))
'''
Exercise 213 - Regular Expressions
Write code on line 5 in order to match 10,259.02 in the string using the search() method.
'''

import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s)

print(result.group(1))

'''
Exercise 214 - Regular Expressions
Write code on line 5 in order to match 17,942,600 BTC in the string using the search() method.
'''

import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r"\s([0-9]{2},[0-9]{3},[0-9]{3}\s.{3}),", s)

print(result.group(1))

'''
Exercise 215 - Regular Expressions
Write code on line 5 in order to match 24h: 0.10% in the string using the search() method.
'''

import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r'24h: \d+\.\d+%', s)


print(result.group())

'''
Exercise 216 - Regular Expressions
Write code on line 5 in order to match Volume 24h: $15,670,986,269 in the string using the search() method.
'''

import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r"\.\d\d, (.{1,}:\s\$\d{2,},\d{2,},\d{2,},\d{2,}), ", s)

print(result.group(1))

'''
Exercise 217 - Regular Expressions
Write code on line 5 in order to match Circulating Supply: 17,942,600 BTC in the string using the search() method.

'''

import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r"(\w+ \w+: \d{2}.+? [A-Z]{3}), ", s)

print(result.group(1))

'''
Exercise 218 - Regular Expressions
Write code on line 5 in order to match 259.02, V in the string using the search() method.
'''
import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

result = re.search(r",([0-9]{3}\.[0-9]{2},\s.)", s)

print(result.group(1))

'''
Exercise 219 - Regular Expressions
Write code on line 5 in order to match all the years in the string using the findall() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\s(\d{4})", s)

print(result)
'''
Exercise 220 - Regular Expressions
Write code on line 5 in order to match all the numbers (3, 2009, 2017 etc.) in the string using the findall() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\d{1,}", s)

print(result)
'''

Exercise 221 - Regular Expressions
Write code on line 5 in order to match all the three-letter words in the string using the findall() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\s(\w{3})\s", s)

print(result)


'''
Exercise 222 - Regular Expressions
Write code on line 5 in order to match all the words starting with an uppercase letter in the string using the findall() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"([A-Z]{1}.+?)\s", s)

print(result)


'''
Exercise 223 - Regular Expressions
Write code on line 5 in order to match all the two-letter words starting with the letter o in the string using the findall() method.
'''
import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\s(o.{1})\s", s)

print(result)
'''
Exercise 224 - Regular Expressions
Write code on line 5 in order to match all the words that have at least 8 characters in the string using the findall() method.
'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\w{8,}", s)

print(result)

'''
Exercise 225 - Regular Expressions
Write code on line 5 in order to match all the words starting with a or c and that have at least 3 letters in the string using the findall() method.

'''

import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result = re.findall(r"\s([ac]\w{2,})\s", s)

print(result)