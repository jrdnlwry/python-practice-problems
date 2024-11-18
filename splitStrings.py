"""
CodeWars: 6Kyu Kata Training

Complete the solution so that it splits the string into pairs of two characters.

If the string contains an odd number of characters then it should replace the missing second -
- character of the final pair with an underscore ('_').
"""


def solution(s):
    listr = []
    for i in range(0, len(s), 2):
        if len(s[i:i+2]) == 2:
            listr.append(s[i:i+2])
        else:
            listr.append(s[i:i+2]+"_")
    return listr



e = solution("asdfadsf")

print(e)
