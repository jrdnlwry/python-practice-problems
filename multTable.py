# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""

tableInput = 4

# initializing a list with a for loop
myList = []
# iterate over a sequence of numbers from 0 to our input
for i in range(tableInput):
  # within each iteration at a list to the main list
  myList.append([])

print(myList)

for i in range(1, tableInput+1):
  #print(i)
  myList[0].append(i)