from datetime import date


def turnHundred(firstName, age):
    """
    This function accepts two arguments
    firstName: string input
    age: int input
    """
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
