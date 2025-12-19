#import data as d
#print(data.prob_1)

#import data as d
#print(d.prob_1)


# from data import prob_1, prob_10, prob_13


from data import *
import re

# problem 1
pattern = re.compile(r'abc')

for string in prob_1:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")

# problem 4
pattern = re.compile(r'[^b]og')

for string in prob_4:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")

# problem 12
pattern = re.compile(r'(\w+ (\d+))')

for string in prob_12:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")

# problem 14
pattern = re.compile(r'I love (cats|dogs)')

for string in prob_14:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")

# problem 5
pattern = re.compile(r'[A-C][n-p][a-c]')

for string in prob_5:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")

# problem 6
pattern = re.compile(r'waz{3,5}up')

for string in prob_6:
    result = pattern.match(string)
    if result is None:
        print(string + " does not match")
    else:
        print(string + " matched")
