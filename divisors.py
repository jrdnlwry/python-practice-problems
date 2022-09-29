def divisor(num):
    
    """
    This function accepts a parameter and returns all values that are 
    divisible by that value.
    num: INT
    """
    for i in range(2, num + 1):
        if num % i == 0:
          print(i)

# exception handling
while True:
  try:
    # if the parameter isn't a number
    # prompt the user to input a number and continue
    divisor(int(input("Please input a number: ")))
    break
  except ValueError:
    print("Please input a number this time!")
