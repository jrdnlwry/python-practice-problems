import re
"""
accept a string as an input
check the length of the string - if > 14 then False - else continue with checks

for each item in the string index:
	is it a "(" if so go to the next char
	is it a num if so go to the next char
	otherwise cancel
"""
def valid_phone_number(phone_number):
  n = "[0-9]"
  p1 = "\("
  p2 = "\)"
  s = " "
  h = "-"

  if len(phone_number) > 14 or len(phone_number) < 14:
    return False
  if re.search(p1,phone_number[0]) == None:
    return False
  elif re.search(n,phone_number[1]) == None:
    return False
  elif re.search(n,phone_number[2]) == None:
    return False
  elif re.search(n,phone_number[3]) == None:
    return False
  elif re.search(p2,phone_number[4]) == None:
    return False
  elif re.search(s,phone_number[5]) == None:
    return False
  elif re.search(n,phone_number[6]) == None:
    return False
  elif re.search(n,phone_number[7]) == None:
    return False
  elif re.search(n,phone_number[8]) == None:
    return False
  elif re.search(h,phone_number[9]) == None:
    return False
  elif re.search(n,phone_number[10]) == None:
    return False
  elif re.search(n,phone_number[11]) == None:
    return False
  elif re.search(n,phone_number[12]) == None:
    return False
  elif re.search(n,phone_number[13]) == None:
    return False
  else:
    return True
  
valid_phone_number("(098) 123 4567")