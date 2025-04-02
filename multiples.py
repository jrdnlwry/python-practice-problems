def solution(number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Additionally, if the number is negative, return 0.

    Note: If the number is a multiple of both 3 and 5, only count it once.
    """    
    n = number
    m1 = 3
    m2 = 5
    m = []

    for i in range(m1, n):
        if i % m1 == 0 or i % m2 == 0:
            m.append(i)
    
    sum = 0
    for n in m:
        sum += n

    return sum


solution(int(input()))