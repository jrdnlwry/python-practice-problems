"""
Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0. 
Your function only needs to return the result
Grasshopper - Summation 8 kyu - Codewars

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

"""

class Addr:
    def __init__(self, num):
        self.num = num

    def summation(self):
        result = 0
        for i in range(0, self.num+1):
            #print(i)
            result += i
        return result
    
numResult = Addr(100)
print(numResult.summation())