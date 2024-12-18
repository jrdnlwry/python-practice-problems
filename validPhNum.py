"""
Refactored code from the following codewars challenge:
# Code Wars: https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python
"""
import re

def valid_phone_number(phone_number):

  if len(phone_number) > 14 or len(phone_number) < 14:
    return False

  if re.search("(\()([0-9]{3})(\))(?!\n)(\s)([0-9]{3})(-)([0-9]{4})", phone_number) == None:
    return False
  else:
    return True
  
valid_phone_number("(333) 185-0594")