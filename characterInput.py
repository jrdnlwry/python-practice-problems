from datetime import date


def turnHundred(firstName, age):
    """
    This function accepts two arguments
    firstName: string input
    age: int input
    """
    

    def testfirstName(firstName):
      """
      This function accepts one argument (firstname)
      It then checks to see whether or not the input is a string
      """

      is_Int = True
      try:
          int(firstName)
      except ValueError:
          is_Int = False
      if is_Int:
          # if the input is an integer prompt the user for their name again 
          firstName = input("Ooops you entered a number please give me your first name this time: ")
          return firstName
      else:
          # if the input variable is a string return the input and continue
          return firstName
    
    def testAge(age):
      """
      This function accepts age input and test whether or not it is an integer
      """
      is_Int = True
      try:
          int(age)
      except ValueError:
          is_Int = False
      if is_Int:
          return age
      else:
          age = input("Ooops you entered a string please give me your age this time: ")
          return age

    # call first Name and age testing function
    # set the returned value as a firstName variable
    firstName = testfirstName(firstName)
    # set the returned value as age variable
    age = testAge(age)
    
    # set a dynamic variable: current year
    currentYear = date.today().year
    # convert the persons age into an integer
    age = int(age)
    # subtract 100 from their age
    formula = 100 - age
    # this formula calculates the future year when they will turn 100
    futureYear = currentYear + formula
    print()
    # print when they will turn 100
    print(f"""{firstName} you will turn 100 in {formula} years.\n\nOr in the year {futureYear}""")
    
# call the function with the required inputs
turnHundred(input("Please give us your first name: "), input("What is your age: "))
