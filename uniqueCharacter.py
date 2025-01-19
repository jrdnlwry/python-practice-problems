"""
This problem has a single exercise worth a total of ten (10) points.

Exercise 0 (10 points). Define a function, UniqueCharacters(s), that given a string s returns a tuple of two elements: the first element is the number of unique alphabetic characters in the string and the second is the number of unique digits (base-10) in the string.

For example, the string 'ewwwffioj122434' should output the following tuple: (6, 4). The 6 occurs because there are 6 unique letters ('e', 'w', 'f', 'i', 'o', and 'j') and 4 because there are 4 unique decimal digits ('1', '2', '3', '4'). Special characters may appear in the string but do not count as a letter or number.

-------------------->

IDEAS to solve:

# identify different data types:

- use Regex to distinguish between Integers & Strings

# store the data types into two separate sets

- after identifying the Strings store them in their own sets
- repeat for the integers

# return a Tuple of the number of values in the two elements
- find the len of each data structure and return it as a tuple

- [a-zA-Z]: matches any character in the range A-Z or a-z
- [[:alpha:]]: matches all string values
- \d: matches any digit

"""

import re
import copy

def UniqueCharacters(s):
    ###
    ### YOUR CODE HERE
    ###
    
    strVal = copy.deepcopy(s)

    x = re.findall("[a-zA-Z]",strVal)
    y = re.findall("\d",strVal)
    # put each result into a set to get unique values
    X = set(x)
    Y = set(y)
    # len(X)

    # return a tuple of the length of each data structure
    T = (len(X), len(Y))
    
    return T

"""
'abc1234'
''
'9090909p0y90p90y90'
"""