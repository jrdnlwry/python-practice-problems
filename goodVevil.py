# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

"""
Accept two inputs
	input 1: total power of good
	input 2: total power of evil

for each string input
	split each character
	convert it to an integer
	count the occurrences of each race for good and evil factions
	update the dictionary accordingly
	calculate the total value
	

Next, sum the total up on each side to determine who wins
"""

def good_vs_evil(good, evil):

  goodDict = {
      'hobbits': {
          'count': 0,
          'value': 1
      },
      'Men': {
          'count': 0,
          'value': 2
      },
      'Elves': {
          'count': 0,
          'value': 3
      },
      'Dwarves': {
          'count': 0,
          'value': 3
      },
      'Eagles': {
          'count': 0,
          'value': 4
      },
      'Wizards': {
          'count': 0,
          'value': 10
      }
  }

  evilDict = {
      'orcs': {
          'count': 0,
          'value': 1
      },
      'Men': {
          'count': 0,
          'value': 2
      },
      'wargs': {
          'count': 0,
          'value': 2
      },
      'goblines': {
          'count': 0,
          'value': 2
      },
      'uruk hai': {
          'count': 0,
          'value': 3
      },
      'trolls': {
          'count': 0,
          'value': 5
      },
      'wizards': {
          'count': 0,
          'value': 10
      }
  }

  goodTotal = 0
  evilTotal = 0

  good = good.split(" ")
  evil = evil.split(" ")

  for g, num in zip(goodDict, good):
    goodDict[g]['count'] += int(num)

  for i in goodDict:
    goodTotal += goodDict[i]["count"] * goodDict[i]["value"]

  for e, num in zip(evilDict, evil):
    evilDict[e]['count'] += int(num)

  for i in evilDict:
    evilTotal += evilDict[i]["count"] * evilDict[i]["value"]
   
  if goodTotal > evilTotal:
    return "Battle Result: Good triumphs over Evil"
  elif goodTotal < evilTotal:
    return "Battle Result: Evil eradicates all trace of Good"
  else:
    return "Battle Result: No victor on this battle field"