"""
Code wars: Simple fun #176 Reverse Letter 

Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string

"""
# import string library function  
import string  
    
# Storing the sets of punctuation in variable result  
result = string.punctuation 



def reverse_letter(str):
  sequence = []
  reversedArr = []
  StrText = []

  for i in str:
    if not i.isnumeric() and not i in string.punctuation:
        StrText.append(i)

  "".join(StrText)

  for i in range(len("".join(StrText))):
    sequence.append(i)

  sequence.sort(reverse=True)

  for i in sequence:
    reversedArr.append("".join(StrText)[i])

  return "".join(reversedArr).replace(" ","")

strReverse = reverse_letter(input())

print(strReverse)