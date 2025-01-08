def find_it(seq):
    """
    Given an array of integers, find the one that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.

    Approach:
    accept an input of integers
    create a dictionary object
    remove all duplicates of integers and save to the dictionary object
    count the occurrences of all integers from original list
	- save how many times they occur within the dictionary
    """
    myDict = {}
    uniqueValues = list(set(seq))
  
    for i in uniqueValues:
        myDict[i] = seq.count(i)
    oddInt = 0
    for i in myDict:
        if myDict[i] % 2 != 0:
            oddInt = i

    return oddInt


