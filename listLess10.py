# list variable of integers
numList = [1, 2, 3, 4, 5, 10, 12, 54, 100]
# new empty list
newList = []

def lessThan(num):
  """
  this function accepts a keyword arguement
  num: INT variable
  """
  # check if a integer is less than 10
  if num < 10:
    # if it is less than 10 append it to the list variable
    newList.append(num)

for num in numList:
  lessThan(num)

print(newList)
