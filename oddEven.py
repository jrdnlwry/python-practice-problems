def oddEven(num):
  """
  This function accepts one variable
  There's currently no exception handling
  num: INT input
  """
  # convert accepted number into an integer
  num = int(num)
  # use modulo to get the remainder after dividing by 2
  if num % 2 == 0:
    # if it is divisible by 2 (if the remainder is 0)
    print("You gave an even number")
  else:
    # otherwise the number is odd
    print("You gave an odd number")

oddEven(input("input a number: "))
