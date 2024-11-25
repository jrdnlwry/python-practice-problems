"""
There is an array with some numbers.

All numbers are equal except for one. Try to find it!
"""
def find_uniq(arr):
    t = []
    # iterate through the list element and append unique values to the
    # previously created blank list
    for i in arr:
        if i in t:
            pass
        else:
            t.append(i)

    for n in t:
        if arr.count(n) == 1:
            return n # n: unique number in the array