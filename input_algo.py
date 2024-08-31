# 1.) Each student receives a grade in the inclusive range from 0 to 100
# 2.) any grade less than 40 is failing

# Grades get rounded according to the following:

# If the difference between the `grade` and the next multiple of 5 is less than 3, round `grade` up to the next multiple of 5.

# If the value of `grade` is less than 38, no rounding occurs as the result will be a failing grade.


# Examples

# grade = 84: ROUND UP to 85 (85-84 is less than 3)
# grade = 29: DO NOTHING (result is > 40)
# grade = 57: DO NOT ROUND (60 - 57 is 3 or higher)

# accept an input
gradeInput = int(input())
# store the result of each iteration
gradeVar = 0
# initialize an empty variable to hold multiple of gradeInput
multVar = 0
# finalGrade
finalGrade = 0

def GradingStudents(grades):

  gradeVar = gradeInput
  # Loop infinitely
  while True:
      # Increment the counter
      gradeVar += 1
      print(f"Count is {gradeVar}")

      # Check if the counter has reached a certain value
      if gradeVar % 5 == 0:
          # If so, exit the loop
          multVar = gradeVar
          break

  # This will be executed after the loop exits
  print("The loop has ended.")

  # subtract multVar - gradeInput 
  resultVar = multVar - gradeInput
  ##  if < 3 then gradeInput = multVar
  if gradeInput < 40:
    finalGrade = 0
  elif resultVar < 3:
    finalGrade = multVar
  ##  elif >= 3: no rounding
  elif resultVar >= 3:
    finalGrade = gradeInput
  ##  else: do nothing fail
  else:
    print("do nothing")

  return finalGrade

finalGradeScore = GradingStudents(gradeInput)
print()
print("final grade is:", finalGradeScore)