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

# def good_vs_evil(good, evil):
#   g = 0
#   e = 0
#   good = good.split(" ")
#   evil = evil.split(" ")
#   for a in (good):
#     g += int(a)
#   for b in (evil):
#     e += int(b)
#   print(g)
#   print(e)

#   if g > e:
#     return "Battle Result: Good triumphs over Evil"
#   elif g < e:
#     return "Battle Result: Evil eradicates all trace of Good"
#   else:
#     return "Battle Result: No victor on this battle field"

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

# testing
print(goodDict)

good = '1 0 0 0 1 0'
good = good.split(" ")

for g, num in zip(goodDict, good):
  goodDict[g]['count'] += int(num)

print(goodDict)